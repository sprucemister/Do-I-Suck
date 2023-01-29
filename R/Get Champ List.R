get_champ_list <- function(my_df, my_summonerName) {
  my_df %>% 
    filter(summonerName==my_summonerName) %>% 
    group_by(championName) %>%
    summarize(cnt=n(), .groups='drop') %>% 
    arrange(desc(cnt)) %>% 
    select(championName) %>%
    distinct() %>%
    pull(championName)
}