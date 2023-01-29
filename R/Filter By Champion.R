filter_by_champion <- function(my_df, my_champion_list) {
  if (is.null(my_champion_list)) {
    return(my_df)
  } else {
    my_df %>%
      filter(championName %in% my_champion_list) %>%
      return()
  }
}