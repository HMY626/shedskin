#new casting/conversion approach
digit_dict = {
              "1":{1:(1,2,3,4,5),2:(1,3,5)  ,3:()}
              ,"2":{1:(2,)           ,2:()          ,3:(4,)}
              ,"3":{1:(2,4)         ,2:()          ,3:()}
              ,"4":{1:(4,5)         ,2:(1,5)     ,3:()}
              ,"5":{1:(4,)           ,2:()          ,3:(2,)}
              ,"6":{1:()              ,2:()          ,3:(2,)}
              ,"7":{1:(2,3,4,5)  ,2:(3,5)     ,3:()}
              ,"8":{1:()              ,2:()          ,3:()}
              ,"9":{1:(4,)           ,2:()          ,3:()}
              ,"0":{1:()              ,2:(3,)       ,3:()}
}
for d in sorted(digit_dict):
    d2 = digit_dict[d]
    for e in sorted(d2):
        print d, e, d2[e]

l = [[7,8,9], [7.7,8.8,9.9]]
    
for ll in l:
    for lll in ll:
        print '%.2f' % lll

#circular includes
from testdata import bert
class Here:
    def __str__(self):
        return 'here'
bert.hello(Here())
