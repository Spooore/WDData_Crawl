library(ggplot2)
library(dplyr)
library(readr)
Consolidated <- read_delim("Documents/PythonProjects/WDGTDC/WDData_Crawl/Consolidated.csv", 
                           "#", escape_double = FALSE, trim_ws = TRUE)
View(Consolidated)

