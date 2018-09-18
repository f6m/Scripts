#install.packages('ggplot2')
#install.packages('reshape2')
#https://davetang.org/muse/2017/02/03/gantt-chart-using-r/

library(reshape2)
library(ggplot2)
rm(list = ls())

task1 <- c('Cuestionario', '2018-10-01', '2018-10-08') #6 dias
task2 <- c('Herramientas de Software', '2018-10-09', '2018-10-13') #3 dias
task3 <- c('Foro/Wiki', '2018-10-14', '2018-11-14') #30 dias
task4 <- c('Notas', '2018-10-01', '2018-11-25') # 40 dias
task5 <- c('Divulgacion', '2018-11-01', '2018-11-15') # 15 dias
task6 <- c('Retroalimentaciones', '2018-10-02', '2018-12-02') # 60 dias

df <- as.data.frame(rbind(task1, task2, task3, task4, task5, task6))
names(df) <- c('Actividad', 'Inicio', 'Fin')
df$Actividad <- factor(df$Actividad, levels = df$Actividad)
df$Inicio <- as.Date(df$Inicio)
df$Fin <- as.Date(df$Fin)
df_melted <- melt(df, measure.vars = c('Inicio', 'Fin'))

# starting date to begin plot
start_date <- as.Date('2018-10-01')

ggplot(df_melted, aes(value, Actividad)) + 
  geom_line(size = 10) +
  labs(x = '', y = '', title = 'Cronograma de Actividades') +
  theme_bw(base_size = 22) +
  theme(plot.title = element_text(hjust = 0.5),
        panel.grid.major.x = element_line(colour="black", linetype = "dashed"),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text.x = element_text(angle = 78)) +
  scale_x_date(date_labels = "%Y %b", limits = c(start_date, NA), date_breaks = '1 week')

# see ?strptime if you want your date in a different format
# see http://docs.ggplot2.org/current/scale_date.html if you want to adjust the x-axis