def get_api_data(summoner_name, region):

  # Packages
  from riotwatcher import LolWatcher, ApiError
  import time
  import pandas as pd
  import datetime
  
  # Helper Functions
  def epoch_as_date(ts_epoch):
    return datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')

  # Inputs
  lol_watcher = LolWatcher('RGAPI-83206e5d-fd32-47c4-83bd-a25788816e10') # API Key
  my_region = region
  my_summoner_name = summoner_name
  
  # Get My ID
  me = lol_watcher.summoner.by_name(my_region, my_summoner_name)
  print(me)
  
  # Times to interate through in batches for match ID's
  start_time = 1654045261 # Wednesday, June 1, 2022 1:01:01 AM GMT
  interval_time = 2592000 # Approximately 1 month of seconds in epoch seconds
  end_time = round(time.time())
  
  # Initialize Output Data Frame
  my_col_list=['teamPosition','soloKills','championName','win','summonerName' \
                ,'kda','gameCreation']
  df = pd.DataFrame(columns=my_col_list)
  
  # Loop through appx 1 month intervals to get 100 matches per month
  for batch_start_time in range(start_time, end_time, interval_time):
    print(epoch_as_date(batch_start_time))
    my_match_ids = lol_watcher.match.matchlist_by_puuid(my_region, \
                                                        me['puuid'], \
                                                        type='ranked', \
                                                        count=100, \
                                                        start_time=batch_start_time, \
                                                        end_time=batch_start_time+interval_time)
    my_match_ids_LENGTH = len(my_match_ids)
    if my_match_ids_LENGTH>0:
      for match_id in range(0,my_match_ids_LENGTH):
        print('match_id')
        print(match_id)
        my_match = lol_watcher.match.by_id(my_region, my_match_ids[match_id])
        # View(my_match) # walk through the dictonary
        
        gameCreation = my_match["info"]["gameCreation"] # game start time in epoch seconds
        for participant in range(0,10):
          teamPosition = my_match["info"]["participants"][participant]["teamPosition"] # position
          soloKills = my_match["info"]["participants"][participant]["challenges"]["soloKills"] # solo kills
          championName = my_match["info"]["participants"][participant]["championName"] # champ name
          win = my_match["info"]["participants"][participant]["win"] # win or lose
          summonerName = my_match["info"]["participants"][participant]["summonerName"] # summoner name like w6f
          kda = my_match["info"]["participants"][participant]["challenges"]["kda"] #kda
          
          row_to_append = pd.DataFrame([{'teamPosition':teamPosition, \
                                          'soloKills':soloKills, \
                                          'championName':championName, \
                                          'win':win, \
                                          'summonerName':summonerName, \
                                          'kda':kda, \
                                          'gameCreation':gameCreation}])
                                          
          df = pd.concat([df,row_to_append])
    print('========================================')
    df.to_csv('Temp - Raw API Data.csv', index=False)
