# visualize_data.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from datetime import datetime
from config import CLOUD_PROVIDERS, TICKERS

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def get_top_providers(performance_df, n=10):
    """Get the top n cloud providers by market presence or data points."""
    if 'data_points' in performance_df.columns:
        # Sort by number of data points (proxy for market presence)
        return performance_df.sort_values('data_points', ascending=False).head(n)
    else:
        # If data_points not available, just take the first n
        return performance_df.head(n)

def plot_stock_price_with_indicators(data, company, output_dir):
    """Create a chart with stock price and key technical indicators."""
    # Get company and service names
    company_info = CLOUD_PROVIDERS.get(company, {'company': company, 'service': company})
    company_name = company_info['company']
    service_name = company_info['service']
    
    # Filter data for the company
    company_data = data[data['Company'] == company].sort_values('Date')
    
    if len(company_data) < 20:
        print(f"Not enough data for {service_name} to create meaningful visualizations")
        return
    
    # Create a plot with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1, 1]})
    fig.suptitle(f'{service_name} ({company_name}) Stock Price and Technical Indicators', fontsize=16)
    
    # Plot 1: Stock price with moving averages
    ax1.plot(company_data['Date'], company_data['Close'], label='Close Price', color='blue')
    ax1.plot(company_data['Date'], company_data['SMA_20'], label='SMA 20', color='red', alpha=0.7)
    ax1.plot(company_data['Date'], company_data['SMA_50'], label='SMA 50', color='green', alpha=0.7)
    ax1.plot(company_data['Date'], company_data['SMA_200'], label='SMA 200', color='purple', alpha=0.7)
    ax1.set_title(f'Stock Price History')
    ax1.set_ylabel('Price')
    ax1.grid(True)
    ax1.legend()
    
    # Plot 2: RSI
    ax2.plot(company_data['Date'], company_data['RSI'], color='orange')
    ax2.axhline(y=70, color='red', linestyle='--', alpha=0.5)
    ax2.axhline(y=30, color='green', linestyle='--', alpha=0.5)
    ax2.set_title('RSI (Relative Strength Index)')
    ax2.set_ylabel('RSI')
    ax2.grid(True)
    ax2.set_ylim(0, 100)
    
    # Plot 3: MACD
    ax3.plot(company_data['Date'], company_data['MACD'], label='MACD', color='blue')
    ax3.plot(company_data['Date'], company_data['MACD_Signal'], label='Signal', color='red', alpha=0.7)
    ax3.bar(company_data['Date'], company_data['MACD_Histogram'], label='Histogram', color='green', alpha=0.5)
    ax3.set_title('MACD (Moving Average Convergence Divergence)')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('MACD')
    ax3.grid(True)
    ax3.legend()
    
    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    
    # Save the figure
    output_path = os.path.join(output_dir, f'{company}_{company_name.replace(" ", "_")}_technical_analysis.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Chart saved for {service_name}")
    
    return output_path

def plot_performance_comparison(performance_df, output_dir):
    """Create comparison charts of cloud provider performances."""
    # Ensure we have data
    if performance_df.empty:
        print("No performance data available")
        return
    
    # Select relevant columns for comparison
    metrics = ['month_return', 'three_month_return', 'six_month_return']
    metric_names = {"month_return": "1-Month Return", 
                    "three_month_return": "3-Month Return", 
                    "six_month_return": "6-Month Return"}
    
    # Get top 10 companies by data points
    top_companies = get_top_providers(performance_df)
    
    # Create a figure for each metric
    for metric in metrics:
        if metric not in performance_df.columns:
            continue
            
        plt.figure(figsize=(12, 8))
        
        # Create a dataframe for plotting with service names
        plot_df = top_companies.copy()
        if 'service_name' in plot_df.columns:
            plot_df = plot_df.sort_values(metric, ascending=False)
            
            # Create horizontal bar chart
            colors = sns.color_palette("viridis", len(plot_df))
            bars = plt.barh(y=plot_df['service_name'], width=plot_df[metric], color=colors)
            
            # Add values and company tickers to the bars
            for i, bar in enumerate(bars):
                width = bar.get_width()
                ticker = plot_df.index[i]
                plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                        f"{width:.2f}% ({ticker})", 
                        va='center')
        else:
            # Fallback if service names not available
            plot_df = top_companies.sort_values(metric, ascending=False)
            plt.barh(y=plot_df.index, width=plot_df[metric])
        
        # Set titles and labels
        metric_name = metric_names.get(metric, metric.replace('_', ' ').title())
        plt.title(f'Top 10 Cloud Providers by {metric_name}', fontsize=16)
        plt.xlabel('Return (%)')
        plt.ylabel('Cloud Provider')
        plt.grid(True, axis='x')
        
        # Save the figure
        output_path = os.path.join(output_dir, f'top_providers_by_{metric}.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Performance comparison chart saved for {metric}")
    
    # Create a comparison of volatility vs return
    if 'volatility' in performance_df.columns and 'three_month_return' in performance_df.columns:
        plt.figure(figsize=(12, 10))
        
        # Create a scatter plot
        if 'service_name' in top_companies.columns:
            scatter = plt.scatter(
                x=top_companies['volatility'], 
                y=top_companies['three_month_return'],
                s=100,
                c=range(len(top_companies)),
                cmap='viridis',
                alpha=0.7
            )
            
            # Add service name labels
            for i, (idx, row) in enumerate(top_companies.iterrows()):
                plt.annotate(
                    row['service_name'],
                    (row['volatility'] + 0.05, row['three_month_return'] + 0.05),
                    fontsize=9
                )
        else:
            # Fallback if service names not available
            scatter = plt.scatter(
                x=top_companies['volatility'], 
                y=top_companies['three_month_return'],
                s=100,
                alpha=0.7
            )
            
            # Add ticker labels
            for i, (idx, row) in enumerate(top_companies.iterrows()):
                plt.annotate(
                    idx,
                    (row['volatility'] + 0.05, row['three_month_return'] + 0.05),
                    fontsize=9
                )
        
        # Add a trend line
        z = np.polyfit(top_companies['volatility'], top_companies['three_month_return'], 1)
        p = np.poly1d(z)
        plt.plot(
            top_companies['volatility'], 
            p(top_companies['volatility']), 
            "r--", 
            alpha=0.7
        )
        
        # Set titles and labels
        plt.title('Risk vs. Return: Top 10 Cloud Providers', fontsize=16)
        plt.xlabel('Volatility (Risk)')
        plt.ylabel('3-Month Return (%)')
        plt.grid(True)
        
        # Save the figure
        output_path = os.path.join(output_dir, 'risk_vs_return_top_providers.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        print("Risk vs. Return chart saved")

def plot_correlation_matrix(correlation_df, display_corr, output_dir):
    """Visualize the correlation matrix as a heatmap."""
    # Ensure we have data
    if correlation_df.empty:
        print("No correlation data available")
        return
    
    # Get top 10 cloud providers
    correlation_top10 = display_corr.iloc[:10, :10]
    
    # Create the figure
    plt.figure(figsize=(12, 10))
    
    # Create the heatmap
    mask = np.triu(np.ones_like(correlation_top10, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    sns.heatmap(
        correlation_top10, 
        mask=mask,
        cmap=cmap,
        vmax=1, 
        vmin=-1,
        center=0,
        annot=True, 
        fmt=".2f",
        square=True, 
        linewidths=.5,
        cbar_kws={"shrink": .5}
    )
    
    # Set title
    plt.title('Correlation Matrix of Top 10 Cloud Providers', fontsize=16)
    
    # Save the figure
    output_path = os.path.join(output_dir, 'correlation_matrix_top10.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Top 10 correlation matrix visualization saved")

def plot_trend_analysis(trend_counts, output_dir):
    """Visualize the trend analysis."""
    # Ensure we have data
    if trend_counts.empty:
        print("No trend data available")
        return
    
    # Get top 10 cloud providers
    if 'CompanyName' in trend_counts.columns and 'ServiceName' in trend_counts.columns:
        # Get the top providers by total days analyzed
        trend_data = trend_counts.copy()
        trend_data['total_days'] = trend_data['Uptrend'] + trend_data['Downtrend'] + trend_data['Sideways']
        top10_trends = trend_data.sort_values('total_days', ascending=False).head(10)
        
        # Extract just the trend data (not percentages)
        plot_data = top10_trends[['Uptrend', 'Downtrend', 'Sideways', 'ServiceName']].set_index('ServiceName')
    else:
        # Fallback if service names not available
        trend_data = trend_counts.copy()
        if 'Uptrend' in trend_data.columns and 'Downtrend' in trend_data.columns and 'Sideways' in trend_data.columns:
            trend_data['total_days'] = trend_data['Uptrend'] + trend_data['Downtrend'] + trend_data['Sideways']
            top10_trends = trend_data.sort_values('total_days', ascending=False).head(10)
            plot_data = top10_trends[['Uptrend', 'Downtrend', 'Sideways']]
        else:
            print("Required trend columns not found")
            return
    
    # Create a stacked bar chart
    plot_data.plot(
        kind='bar', 
        stacked=True, 
        figsize=(12, 8),
        colormap='viridis'
    )
    
    # Set titles and labels
    plt.title('Trend Analysis: Top 10 Cloud Providers', fontsize=16)
    plt.xlabel('Cloud Provider')
    plt.ylabel('Number of Days')
    plt.legend(title='Trend')
    plt.grid(True, axis='y')
    plt.xticks(rotation=45, ha='right')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the figure
    output_path = os.path.join(output_dir, 'trend_analysis_top10.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print("Top 10 trend analysis visualization saved")

def create_cloud_provider_dashboard(performance_df, correlation_df, trend_counts, output_dir):
    """Create a comprehensive dashboard of the top cloud providers."""
    # Get top 10 providers
    top_providers = get_top_providers(performance_df)
    
    if 'service_name' not in top_providers.columns:
        print("Service name information not available for dashboard")
        return
    
    # Create a dashboard figure
    fig, axs = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('Cloud Provider Market Analysis Dashboard', fontsize=24)
    
    # 1. Performance comparison (top-left)
    if 'three_month_return' in top_providers.columns:
        sorted_df = top_providers.sort_values('three_month_return', ascending=False)
        colors = sns.color_palette("viridis", len(sorted_df))
        bars = axs[0, 0].barh(sorted_df['service_name'], sorted_df['three_month_return'], color=colors)
        
        # Add values to bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ticker = sorted_df.index[i]
            axs[0, 0].text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                        f"{width:.2f}%", va='center')
        
        axs[0, 0].set_title('3-Month Return by Provider', fontsize=16)
        axs[0, 0].set_xlabel('Return (%)')
        axs[0, 0].set_ylabel('Cloud Provider')
        axs[0, 0].grid(True, axis='x')
    
    # 2. Volatility comparison (top-right)
    if 'volatility' in top_providers.columns:
        sorted_df = top_providers.sort_values('volatility')
        colors = sns.color_palette("viridis", len(sorted_df))
        bars = axs[0, 1].barh(sorted_df['service_name'], sorted_df['volatility'], color=colors)
        
        # Add values to bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            axs[0, 1].text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                        f"{width:.2f}", va='center')
        
        axs[0, 1].set_title('Volatility by Provider', fontsize=16)
        axs[0, 1].set_xlabel('Volatility (Standard Deviation)')
        axs[0, 1].set_ylabel('Cloud Provider')
        axs[0, 1].grid(True, axis='x')
    
    # 3. Trend analysis (bottom-left)
    if trend_counts is not None and 'ServiceName' in trend_counts.columns:
        # Join with top providers to get only top 10
        trend_top10 = trend_counts[trend_counts.index.isin(top_providers.index)]
        if not trend_top10.empty:
            # Calculate percentage of each trend type
            trend_data = trend_top10.copy()
            trend_data['total'] = trend_data['Uptrend'] + trend_data['Downtrend'] + trend_data['Sideways']
            trend_data['Uptrend_pct'] = trend_data['Uptrend'] / trend_data['total'] * 100
            trend_data['Downtrend_pct'] = trend_data['Downtrend'] / trend_data['total'] * 100
            trend_data['Sideways_pct'] = trend_data['Sideways'] / trend_data['total'] * 100
            
            # Sort by uptrend percentage
            sorted_trend = trend_data.sort_values('Uptrend_pct', ascending=False)
            
            # Create stacked percentage bar chart
            trends_to_plot = ['Uptrend_pct', 'Sideways_pct', 'Downtrend_pct']
            sorted_trend[trends_to_plot].plot(
                kind='bar', 
                stacked=True, 
                ax=axs[1, 0],
                colormap='viridis'
            )
            
            axs[1, 0].set_title('Trend Distribution by Provider', fontsize=16)
            axs[1, 0].set_xlabel('Cloud Provider')
            axs[1, 0].set_ylabel('Percentage of Days')
            axs[1, 0].legend(['Uptrend', 'Sideways', 'Downtrend'])
            axs[1, 0].set_xticklabels([sorted_trend.loc[idx, 'ServiceName'] for idx in sorted_trend.index], 
                                     rotation=45, ha='right')
            axs[1, 0].grid(True, axis='y')
    
    # 4. Risk-Return scatter plot (bottom-right)
    if 'volatility' in top_providers.columns and 'three_month_return' in top_providers.columns:
        scatter = axs[1, 1].scatter(
            top_providers['volatility'],
            top_providers['three_month_return'],
            s=100,
            c=range(len(top_providers)),
            cmap='viridis',
            alpha=0.7
        )
        
        # Add labels for each point
        for i, (idx, row) in enumerate(top_providers.iterrows()):
            axs[1, 1].annotate(
                row['service_name'],
                (row['volatility'] + 0.05, row['three_month_return'] + 0.05),
                fontsize=9
            )
        
        # Add trend line
        z = np.polyfit(top_providers['volatility'], top_providers['three_month_return'], 1)
        p = np.poly1d(z)
        axs[1, 1].plot(
            top_providers['volatility'],
            p(top_providers['volatility']),
            "r--",
            alpha=0.7
        )
        
        axs[1, 1].set_title('Risk vs. Return', fontsize=16)
        axs[1, 1].set_xlabel('Volatility (Risk)')
        axs[1, 1].set_ylabel('3-Month Return (%)')
        axs[1, 1].grid(True)
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Make room for the suptitle
    
    # Save the dashboard
    output_path = os.path.join(output_dir, 'cloud_provider_dashboard.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Cloud provider dashboard saved")

def main():
    try:
        # Create the figures directory if it doesn't exist
        output_dir = 'stock-analysis-project/results/figures'
        ensure_directory_exists(output_dir)
        
        # Load the analyzed data
        indicators_path = 'stock-analysis-project/data/analyzed/data_with_indicators.csv'
        performance_path = 'stock-analysis-project/data/analyzed/performance_metrics.csv'
        correlation_path = 'stock-analysis-project/data/analyzed/correlation_matrix.csv'
        display_correlation_path = 'stock-analysis-project/data/analyzed/display_correlation_matrix.csv'
        trends_path = 'stock-analysis-project/data/analyzed/trend_analysis.csv'
        
        print("Loading analyzed data...")
        
        # Load data with indicators
        try:
            data = pd.read_csv(indicators_path)
            data['Date'] = pd.to_datetime(data['Date'])
            print(f"Loaded indicators data with shape: {data.shape}")
        except Exception as e:
            print(f"Error loading indicators data: {e}")
            data = None
            
        # Load performance metrics
        try:
            performance_df = pd.read_csv(performance_path, index_col=0)
            print(f"Loaded performance data with shape: {performance_df.shape}")
        except Exception as e:
            print(f"Error loading performance data: {e}")
            performance_df = pd.DataFrame()
            
        # Load correlation matrices
        try:
            correlation_df = pd.read_csv(correlation_path, index_col=0)
            display_corr = pd.read_csv(display_correlation_path, index_col=0) if os.path.exists(display_correlation_path) else correlation_df
            print(f"Loaded correlation data with shape: {correlation_df.shape}")
        except Exception as e:
            print(f"Error loading correlation data: {e}")
            correlation_df = pd.DataFrame()
            display_corr = pd.DataFrame()
            
        # Load trend analysis
        try:
            trend_counts = pd.read_csv(trends_path, index_col=0)
            print(f"Loaded trend data with shape: {trend_counts.shape}")
        except Exception as e:
            print(f"Error loading trend data: {e}")
            trend_counts = pd.DataFrame()
        
        # Generate visualizations
        print("\nGenerating visualizations...")
        
        # 1. Plot technical indicators for top cloud providers
        if data is not None and not performance_df.empty:
            top_providers = get_top_providers(performance_df)
            
            print(f"Creating technical indicator charts for top cloud providers...")
            for provider in top_providers.index:
                try:
                    plot_stock_price_with_indicators(data, provider, output_dir)
                except Exception as e:
                    print(f"Error creating chart for {provider}: {e}")
        
        # 2. Plot performance comparison
        if not performance_df.empty:
            print("Creating performance comparison charts...")
            try:
                plot_performance_comparison(performance_df, output_dir)
            except Exception as e:
                print(f"Error creating performance charts: {e}")
        
        # 3. Plot correlation matrix
        if not correlation_df.empty:
            print("Creating correlation matrix visualization...")
            try:
                plot_correlation_matrix(correlation_df, display_corr, output_dir)
            except Exception as e:
                print(f"Error creating correlation matrix: {e}")
        
        # 4. Plot trend analysis
        if not trend_counts.empty:
            print("Creating trend analysis visualization...")
            try:
                plot_trend_analysis(trend_counts, output_dir)
            except Exception as e:
                print(f"Error creating trend analysis chart: {e}")
        
        # 5. Create comprehensive dashboard
        if not performance_df.empty:
            print("Creating cloud provider dashboard...")
            try:
                create_cloud_provider_dashboard(performance_df, correlation_df, trend_counts, output_dir)
            except Exception as e:
                print(f"Error creating dashboard: {e}")
        
        print("\nVisualization completed successfully!")
        print(f"All charts have been saved to: {output_dir}")
        
    except Exception as e:
        print(f"Error in visualization process: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()