# main.py
import os
import sys
import argparse
from datetime import datetime
import pandas as pd

# Import functions from other scripts
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from download_data import main as download_data
    from process_data import main as process_data
    from analyze_data import main as analyze_data
    from visualize_data import main as visualize_data
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Stock Market Analysis Pipeline for Cloud Providers')
    parser.add_argument('--download', action='store_true', help='Run data download step')
    parser.add_argument('--process', action='store_true', help='Run data processing step')
    parser.add_argument('--analyze', action='store_true', help='Run data analysis step')
    parser.add_argument('--visualize', action='store_true', help='Run data visualization step')
    parser.add_argument('--all', action='store_true', help='Run the entire pipeline')
    
    args = parser.parse_args()
    
    # If no specific steps are specified, run them all
    if not (args.download or args.process or args.analyze or args.visualize):
        args.all = True
        
    return args

def run_pipeline():
    """Run the complete data analysis pipeline."""
    # Parse command line arguments
    args = parse_arguments()
    
    # Start time
    start_time = datetime.now()
    print(f"=== Pipeline started at {start_time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    
    # Create log directory
    log_dir = "stock-analysis-project/logs"
    ensure_directory_exists(log_dir)
    log_file = f"{log_dir}/pipeline_{start_time.strftime('%Y%m%d_%H%M%S')}.log"
    
    # Redirect stdout to log file if not in interactive mode
    if not sys.stdout.isatty():
        sys.stdout = open(log_file, 'w')
    
    try:
        # Step 1: Download Data
        if args.download or args.all:
            print("\n=== Step 1: Downloading Data ===")
            download_result = download_data()
            if download_result is None:
                print("Data download failed. Exiting pipeline.")
                return False
            print("Data download completed successfully.")
        
        # Step 2: Process Data
        if args.process or args.all:
            print("\n=== Step 2: Processing Data ===")
            processed_data = process_data()
            if processed_data is None or processed_data.empty:
                print("Data processing failed. Exiting pipeline.")
                return False
            print("Data processing completed successfully.")
        
        # Step 3: Analyze Data
        if args.analyze or args.all:
            print("\n=== Step 3: Analyzing Data ===")
            analysis_results = analyze_data()
            if analysis_results is None:
                print("Data analysis failed. Exiting pipeline.")
                return False
            print("Data analysis completed successfully.")
        
        # Step 4: Visualize Data
        if args.visualize or args.all:
            print("\n=== Step 4: Visualizing Data ===")
            visualization_result = visualize_data()
            if visualization_result is None:
                print("Data visualization failed. Exiting pipeline.")
                return False
            print("Data visualization completed successfully.")
        
        # Pipeline completion
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"\n=== Pipeline completed at {end_time.strftime('%Y-%m-%d %H:%M:%S')} ===")
        print(f"Total duration: {duration}")
        
        # Generate summary of outputs
        print("\n=== Pipeline Outputs ===")
        print("1. Raw data: stock-analysis-project/data/raw/all_cloud_providers.csv")
        print("2. Processed data: stock-analysis-project/data/processed/stock_data_with_real_dates.csv")
        print("3. Analyzed data: stock-analysis-project/data/analyzed/")
        print("4. Reports: stock-analysis-project/results/reports/analysis_summary.md")
        print("5. Visualizations: stock-analysis-project/results/figures/")
        
        return True
        
    except Exception as e:
        print(f"Pipeline error: {e}")
        return False
        
    finally:
        # Close log file if redirected
        if not sys.stdout.isatty():
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            print(f"Pipeline log saved to {log_file}")

if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)