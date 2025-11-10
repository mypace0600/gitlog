import subprocess
import sys
import textwrap
import os
from datetime import datetime

# --- 설정 ---
AUTHOR_NAME = "hyeonsu"  # git config user.name 과 동일해야 함
PROJECT_PATH = "/Users/jsy94/Desktop/healthnyou"
OUTPUT_DIR = "/Users/jsy94/Desktop"
# --- 설정 끝 ---


def get_git_logs(author_name, project_path):
    """특정 작성자의 오늘 커밋 로그를 가져옴."""
    print(f"🔍 '{project_path}'에서 '{author_name}'의 오늘 로그를 검색합니다...")

    git_command = [
        "git",
        "--no-pager",  # less 방지
        "log",
        "--all",
        f"--author={author_name}",
        "--since=midnight",  # 오늘 0시 이후
        "--pretty=format:- %s"
    ]

    try:
        result = subprocess.run(
            git_command,
            cwd=project_path,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8"
        )
        logs = result.stdout.strip()

        if not logs:
            print("⚠️ 오늘 작업한 커밋 내역이 없습니다.")
            return None

        print("\n--- 📜 오늘의 커밋 목록 ---")
        print(logs)
        print("----------------------------\n")
        return logs

    except subprocess.CalledProcessError as e:
        print(f"❌ Git log 실행 중 오류 발생: {e.stderr}")
        return None
    except FileNotFoundError:
        print("❌ Git 명령을 찾을 수 없습니다. Git이 설치되어 있는지 확인하세요.")
        return None


def summarize_and_save(logs, output_dir):
    """Gemini CLI를 사용해 요약 생성 후 Markdown 파일로 저장."""
    if not logs:
        return

    prompt = textwrap.dedent(f"""
    다음은 오늘 제가 작업한 Git 커밋 목록입니다.
    이 내역을 바탕으로 오늘 한 작업을 전문적인 톤의 업무 요약본(bullet point)으로 만들어주세요.
    중복되는 내용은 합치고 핵심 작업 위주로 정리해주세요.

    [오늘의 커밋 목록]
    {logs}
    """)

    print("💎 Gemini CLI로 요약을 생성 중입니다...\n")

    gemini_command = ["gemini", prompt]

    try:
        result = subprocess.run(
            gemini_command,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8"
        )
        summary = result.stdout.strip()

        today_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{today_str}_summary.md"
        safe_output_dir = os.path.expanduser(output_dir)
        os.makedirs(safe_output_dir, exist_ok=True)
        file_path = os.path.join(safe_output_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {today_str} 작업 요약\n\n")
            f.write(summary)

        print("✅ 요약본 생성 완료!\n")
        print(summary)
        print(f"\n📂 저장 위치: {file_path}\n")

    except subprocess.CalledProcessError as e:
        print(f"❌ Gemini CLI 실행 중 오류 발생: {e.stderr}")
    except FileNotFoundError:
        print("❌ Gemini CLI를 찾을 수 없습니다. 'gemini' 명령이 설치되어 있는지 확인하세요.")
    except Exception as e:
        print(f"⚠️ 파일 저장 중 오류 발생: {e}")


def main():
    if not os.path.exists(PROJECT_PATH):
        print(f"❌ 프로젝트 경로를 찾을 수 없습니다: {PROJECT_PATH}")
        sys.exit(1)

    commit_logs = get_git_logs(AUTHOR_NAME, PROJECT_PATH)

    if commit_logs:
        summarize_and_save(commit_logs, OUTPUT_DIR)
    else:
        print("오늘 커밋이 없어 요약 생성을 건너뜁니다.")


if __name__ == "__main__":
    main()
