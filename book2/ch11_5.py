P_A = 0.01          #疾病率
P_B_given_A = 0.99  #有疾病準確率
# 陽性機率
P_B = 0.01*0.99 + (1 - 0.01)*0.01
#陽性有病機率
P_A_given_B = P_B_given_A * P_A / P_B
print(f"陽性有疾病的機率 {P_A_given_B}")
# 陽性有疾病的機率 0.5
