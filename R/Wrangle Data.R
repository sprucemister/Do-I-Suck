wrangle_data <- function(df, summoner) {
  # Wrangle gameCreation from epoch seconds to datetime
  df <- df %>%
    mutate(gameCreation = as.character(gameCreation)) %>%
    mutate(gameCreation = substr(gameCreation,1,nchar(gameCreation)-3)) %>%
    mutate(gameCreation = as.numeric(gameCreation)) %>%
    mutate(gameCreation = as_datetime(gameCreation))
  
  # Create my_team field
  df <- df %>%
    group_by(gameCreation, win) %>%
    mutate(my_team=any(summonerName==summoner)) %>%
    ungroup()
  
  # Create my_champion field
  df <- df %>%
    filter(summonerName==summoner) %>%
    select(championName, gameCreation) %>% 
    rename(my_champion = championName) %>% 
    inner_join(df, by='gameCreation')
  
  # Calculate my_position column
  df <- df %>%
    group_by(gameCreation, teamPosition) %>%
    mutate(my_position=any(summonerName==summoner)) %>%
    ungroup()
  
  # Filter out bad values
  df <- df %>% 
    filter(is.nan(kda) == FALSE) %>% 
    filter(is.na(kda) == FALSE) %>% 
    filter(is.nan(soloKills) == FALSE) %>% 
    filter(is.na(soloKills) == FALSE) 
}