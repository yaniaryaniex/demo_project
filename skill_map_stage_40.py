# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SkillMap
import argparse

def main():
    parser = argparse.ArgumentParser(description="SkillMap CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    
    # show
    s_show = sub.add_parser("show", help="Show progress")
    s_show.add_argument("--skill", help="Show specific skill")
    
    # start
    s_start = sub.add_parser("start", help="Start a session")
    s_start.add_argument("--skill", required=True)
    s_start.add_argument("--duration", type=int, default=30)
    
    # log
    s_log = sub.add_parser("log", help="Log a result")
    s_log.add_argument("--skill", required=True)
    s_log.add_argument("--result", type=float, default=0)
    s_log.add_argument("--comment", default="")
    
    # stats
    s_stats = sub.add_parser("stats", help="Show statistics")
    s_stats.add_argument("--skill", help="Filter by skill")
    
    args = parser.parse_args()
    
    if args.command == "show":
        show_progress(args.skill)
    elif args.command == "start":
        start_session(args.skill, args.duration)
    elif args.command == "log":
        log_result(args.skill, args.result, args.comment)
    elif args.command == "stats":
        show_statistics(args.skill)

if __name__ == "__main__":
    main()
