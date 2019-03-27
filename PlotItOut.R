library(ggplot2)
library(dplyr)
library(readr)
library(forcats)
Consolidated <- read_delim("Documents/PythonProjects/WDGTDC/WDData_Crawl/Consolidated.csv", 
                           "#", escape_double = FALSE, trim_ws = TRUE)
View(Consolidated)

Consolidated<-Consolidated %>% 
  mutate(Genre=tolower(Genre)) %>% 
  mutate(Genre=sub(" ","",Genre))

PlotData<-Consolidated %>% 
  group_by(`Genre`) %>% 
  filter(`Genre`!="other") %>% 
  summarise(listean_time = sum(`Liczba odsłuchań`)) %>% 
  data.frame()  %>%
  top_n(15)

ggplot(data=PlotData, aes(x = reorder(Genre,-listean_time), y = listean_time, fill = listean_time)) +
  scale_x_discrete() +
  scale_y_continuous() + 
  geom_bar(stat='identity') +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+
  scale_fill_gradient(low = "gold3", high = "red") +
  xlab('Gatunki muzyczne') +
  ylab('Ilość wysłuchań') +
  guides(fill=guide_legend(title="Ilość wysłuchań"))

Mood <- read_delim("Documents/PythonProjects/WDGTDC/WDData_Crawl/Mood.csv", 
                           "#", escape_double = FALSE, trim_ws = TRUE)
View(Mood)

numbers_only <- function(x) !grepl("\\D", x)

PlotMood<-Mood %>% 
  filter(`SpotifyID` != "Cannot Find URI") %>% 
  filter(!numbers_only(SpotifyID)) %>% 
  filter(`Liczba odsłuchań`>1)

PlotMoodText<-Mood %>% 
  filter(`SpotifyID` != "Cannot Find URI") %>% 
  filter(!numbers_only(SpotifyID)) %>% 
  filter(`Liczba odsłuchań`>30) %>% 
  distinct(`Tytuł`, .keep_all = TRUE) 



ggplot(data=PlotMood, aes(x = Energy , y = Valance , color = `Liczba odsłuchań`, size =`Liczba odsłuchań` )) +
  geom_point(alpha = 0.8) +
  geom_label_repel(data=PlotMoodText,
                   aes(label = paste0(`Tytuł`," ",`Artysta`),size=10),
                   box.padding   = 0.1, 
                   point.padding = 0.5,
                   segment.color = 'grey50') +
  scale_x_discrete(breaks=c(0.0,0.5,1.0)) +
  scale_colour_gradient(low = "gold3", high = "red")+
  theme_bw()
