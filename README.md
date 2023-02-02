## Purpose

Answers the age old question "Do I suck or is it my team?" by comparing:

  * Your KDA to your opposing laner's KDA across the same game result
  * Your team's solo kills to their opposing laner's
  
Also provides stats on your solo kills compared to your laners

### API Key

To run with your own API key, make a file called `Get API Key.R` in the folder `/R`
like below where `XXXXX` is your API key:

```r
get_api_key <- function() {
  my_api <- 'XXXXX'
  return(my_api)
}
```
