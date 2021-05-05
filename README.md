# Binary-bot_
# Well before you start this python file just make sure to subscribe and comment
# https://www.youtube.com/channel/UC024Uzg8zcrd5N0lyOPeFRA
# and please watch the installation of the API First .. https://www.youtube.com/watch?v=wNL_io8K4D8
# Run it 
# .."TO MY LATE BIRDS THAT NEVER FAILED TO BE LATE"...
"TO MY YOUNG SELF I DID RESERVE"
# for  begginner's guide # 
# Please Subscribe to My Channel , like and comment and Donate
# install  python ,vscode "optional" but i prefer it and all the extension
# When open folder "binary-bot" 
# start code editor 
# 1 .  line No-10 go=IQ_Option("Email","Password")
# Were go is the container of the API  and IQ_Option() is functioN  that signIN for a user
# Note go is a class contains these different function
# The syntax is  CONTAINER=Class.fuction(paramzA and paramzB ) in this case our class name is " go " and every function require to have to paramz 
# TO CALL IT  CONTAINER.INSIDE(YEAD,HOUSE)

# GAINNING ACCESS TO DATA THAT SCREAM THE CANDLE  line 25 --- go.start_candles_stream(pair,size,maxdict) pair ,size,maxdict  is being defined on top line 23,24
# where a candle size is diffent . 5 minutes and three candle data will give  output of different candle stick .
# The  start_candles_stream() gives you access to a pair ="china/ZAR" the size dictmax="the number of object we want  from the server"
storage_data = go.get_realtime_candles(pair,size)
# after that function you have access to the pair you selected  pair ="china/ZAR" meaning you can get access to pip values hi lo volume min max



 storage_data = go.get_realtime_candles(pair,size)
    # print("Recieving data :" ,  storage_data)

  
    # time.sleep()
    # for stored_data in list(storage_data.keys()):
        
    #     open_=(storage_data[stored_data]['open'])
    #     close=(storage_data[stored_data]['close'])
    #     low=(storage_data[stored_data]['min'])
    #     volume=(storage_data[stored_data]['volume'])
    #     high=(storage_data[stored_data]['max'])

    #     print("###################################")
    #     print("###  ##" +' '+ pair +' '+" #######  #####  ######  ####")
    #     print("###################################")
    #     print("Recieving  open data :" ,open_)
    #     print("Recieving low data :" ,low)
    #     print("Recieving high data :" ,high)
    #     print("Recieving close data :" ,close)
    #     print("Recieving volume data :" ,volume)
    #     print("############### HACKING THE SERVERS  PLEASE WAIT ......####################")
    
    
    Computed_DataModule
   NOT INCLUDED
   
   
   
   
   
   




