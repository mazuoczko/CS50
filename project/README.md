# Tft Data
#### Video Demo:  <https://youtu.be/pFZ3--oz9co>  
#### Description:
##### General purpose. 
My program purpose is analyzing data from popular video game Team Fight Tactic. 
TFT (for short) is a game from kind of auto battlers. Where you putting champions on the bord and let them fight. 
Champions can you find in the shop that is automatically refresh after each round and if you pay 2 gold. Every champion have his cost dependent on their  (1/2/3/4/5). 
Gold is cumulate every round. And increase of gold is calculated depend on interest from gold you have and win streak or lose streak.  
Thanks to that you always need to calculate if your bord is not to week and also you cannot spend to math gold on champions because that gone hurt your economy. 
Because of that is very helpful to know precise watch stats have itch champion and how efficient is itch stats  according to cost.

##### CSV file.
	I decide to use self-made csv file even if JEASON will be better idea unfortunately company that create this game give aces to the JEASON file only to registered companies so I cannot use this data. 
So I create smaller file that is exemplary of how this data is presented on sites where you can read this data. 
I decide to use DictReder for resilience of code. 

##### Frist function (reading_all_stats).
	Purpose of first function is reading all stats that can by important for user. In that function after choosing correct options and writing name of the champion you are getting stats that are saved in csv file.   
In case that user want now stats of every champion he can just write “ all ” and function gone return that data.

##### Secund function (sum_of_stats).
	Similar to previous function after choosing correct options user and writing name of champion user gone get sum of statistic minus mana cost as in that game mana have negative value. 
That function can by helpful in deciding if champion give the best stats according to cost.
In case that user want to now sum of all stats for all champions he also only need write all after choosing correct option.

#####Trid function (cost_efficency).

	Like before after causing correct option and writing a name of the champion user gone get how many stats he is getting for every gold spend. 
That function can be helpful for deciding if invention in more expensive unit is good decision.
Also in this function user can write all to get all information for all champions. 
