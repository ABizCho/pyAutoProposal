import pandas as pd
import datetime


#####
def extractUrlList_from_excel() :
    #             
    DateTime = datetime.datetime.now()
    DateTime = DateTime.strftime('%y%m%d')
    #
    df = pd.read_excel("C:\\Users\\JSW\Desktop\\epichio_blogTask\\blogVisitor_{0}.xlsx".format(DateTime))
    #
    df = df.iloc[:,[1,7]]

    # 방문자수 평균이 1500을 초과하는 블로거 삭제
    df = df[df['방문자수 평균'] <= 1500]
    df.reset_index(drop=True,inplace=True)


    #DF -> 리스트로 변환
    bloggerList = df.values.tolist()
    #
    urlList = list()
    for i in range(len(bloggerList)) : 
        urlList.append(bloggerList[i][0])
    # #
    # rmUrl = "https://blog.naver.com/"
    # for i in range(len(urlList)) :
    #     urlList[i]= urlList[i].replace(rmUrl,'')

    #
    return urlList
