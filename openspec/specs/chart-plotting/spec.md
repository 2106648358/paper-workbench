# Chart Plotting Specification

## Overview
使用 Python + Matplotlib 生成学术统计图，支持散点图、折线图、柱状图等类型。

## ADDED Requirements

### Requirement: Generate scatter plot with individual data points
The system SHALL create scatter plots showing individual subject data points with mean line and error bars.

#### Scenario: Create jump height scatter plot
- **WHEN** user requests scatter plot for jump height data
- **THEN** system generates PNG showing:
  - Individual data points for experiment group (n=10) and control group (n=10)
  - Mean line for each group
  - Error bars showing standard deviation
  - Clear group labels on x-axis

#### Scenario: Create displacement scatter plot
- **WHEN** user requests scatter plot for displacement data
- **THEN** system generates PNG with same structure as jump height plot

### Requirement: Generate line chart showing trends
The system SHALL create line charts connecting pre/post intervention data points to show change trends.

#### Scenario: Create decay rate trend chart
- **WHEN** user requests decay rate trend chart
- **THEN** system generates PNG showing:
  - Lines connecting pre-intervention to post-intervention for each metric
  - Separate lines for experiment group and control group
  - Clear time labels (干预前/干预后)

### Requirement: Generate grouped bar chart with error bars
The system SHALL create grouped bar charts comparing multiple metrics across groups with statistical annotations.

#### Scenario: Create group comparison bar chart
- **WHEN** user requests group comparison chart
- **THEN** system generates PNG showing:
  - Bars for experiment and control groups
  - Error bars for each bar
  - Significance stars (*) for P < 0.05, (**) for P < 0.01
  - Metric labels on x-axis

### Requirement: Use Chinese fonts
The system SHALL render Chinese characters correctly using SimHei font embedded in the output images.

#### Scenario: Chinese labels display correctly
- **WHEN** chart contains Chinese text (e.g., "实验组", "对照组", "干预前")
- **THEN** Chinese characters display correctly without boxes or garbled text
- **AND** font matches SimHei style

### Requirement: Apply fresh color schemes per chart
The system SHALL apply distinct, fresh color schemes to each chart type.

#### Scenario: Jump height chart colors
- **WHEN** generating jump height scatter plot
- **THEN** experiment group uses mint green/blue tones
- **AND** control group uses coral/orange tones

#### Scenario: Displacement chart colors
- **WHEN** generating displacement scatter plot
- **THEN** experiment group uses forest green tones
- **AND** control group uses brick red tones

#### Scenario: Trend chart colors
- **WHEN** generating decay trend chart
- **THEN** experiment group uses cyan-blue gradient
- **AND** control group uses gray-purple gradient

#### Scenario: Bar chart colors
- **WHEN** generating comparison bar chart
- **THEN** experiment group uses deep blue
- **AND** control group uses light gray

### Requirement: Optimize layout for centering
The system SHALL position chart content in the center of the canvas with adequate margins.

#### Scenario: Content centered
- **WHEN** generating any chart
- **THEN** data visualization area is centered horizontally and vertically
- **AND** top margin is approximately 10% of canvas height
- **AND** bottom margin is approximately 20% (for labels/legend)

#### Scenario: Labels not overlapping
- **WHEN** generating charts with legends
- **THEN** legend is positioned outside the data area
- **AND** axis labels do not overlap with tick marks or data points

### Requirement: Output high-resolution PNG
The system SHALL save all charts as PNG files at 300 DPI resolution.

#### Scenario: Save jump height chart
- **WHEN** jump height chart generation completes
- **THEN** file is saved to figures/data-jump-height.png
- **AND** resolution is 300 DPI
- **AND** file size is reasonable (< 2MB)

#### Scenario: Save all charts
- **WHEN** script runs to completion
- **THEN** 4 PNG files are created in figures/ directory:
  - data-jump-height.png
  - data-displacement.png
  - decay-trend.png
  - group-comparison.png

### Requirement: Support academic paper styling
The system SHALL generate charts suitable for academic publication with appropriate styling.

#### Scenario: Professional appearance
- **WHEN** generating charts
- **THEN** font sizes are readable at print scale (8-12pt)
- **AND** line weights are appropriate (1-2pt)
- **AND** colors are not overly saturated (60-80% saturation)
- **AND** charts work in grayscale (color-blind friendly)