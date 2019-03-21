library(ggplot2)
library(dplyr)
library(readr)
Consolidated <- read_delim("Documents/PythonProjects/WDGTDC/WDData_Crawl/Consolidated.csv", 
                           "#", escape_double = FALSE, trim_ws = TRUE)
View(Consolidated)

Consolidated<-Consolidated %>% 
  mutate(Genre=tolower(Genre)) %>% 
  mutate(Genre=sub(" ","",Genre))

PlotData<-Consolidated %>% 
  group_by(`Genre`) %>% 
  summarise(listean_time = sum(`Liczba odsłuchań`)) %>% 
  data.frame()  %>%
  top_n(15)

ggplot(data=PlotData, aes(x = Genre, y = listean_time)) +
  scale_x_discrete() +
  scale_y_continuous() + 
  geom_bar(stat='identity') +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))