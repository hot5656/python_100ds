# 垃圾郵件分類實作
import numpy as np

# 垃圾郵件數據
spam_emails = [
    "Get a free gift card now!",
    "Limited time offer: Claim your prize!",
    "You have won a free iPhone!"
]
# 非垃圾郵件數據
ham_emails = [
    "Meeting rescheduled for tomorrow",
    "Can we discuss the repoet later?",
    "Thank you for your prompt reply."
]

# 單詞計算
def count_words(emails):
    word_count= {}
    for email in emails:
        for word in email.split():
            word = word.lower()
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    return word_count


# check email 型別
# 使用 ln(log 底數e)算機率的優點
# 1. 避免數值下溢：當計算多個小機率值的乘積時，避免結果變得極小。
# 2. 計算穩定性：轉換為求和運算使得計算更加穩定。
# 3. 簡化比較：分類時直接比較對數和，比比較原始機率乘積更簡單。
def classify_email(email):
    words = email.lower().split()
    spam_prob = np.log(prior_spam)
    ham_prob = np.log(prior_ham)
    # print(f"spam_prob={prior_spam}{spam_prob}")
    # print(f"ham_prob={prior_ham}{ham_prob}")
    for word in words:
        # word 存在 get word value, 不存在 get 1/ (total_spam_words+2)
        spam_prob += np.log(spam_word_prob.get(word, 1/ (total_spam_words+2)))
        ham_prob += np.log(ham_word_prob.get(word, 1/ (total_ham_words+2)))
    print(f"spam_prob:{spam_prob} ham_prob:{ham_prob}")
    return "垃圾郵件" if spam_prob > ham_prob else "非垃圾郵件"

# 計算每個字的機率, +1 避免機率為零的情況, 分母 +2 而不是+1，是為了更好的平滑效果。
# 這樣做的目的是考慮訓練數據中未出現過的單詞。實際上，+2 是一個常見的變種，
# 但你也可以看到其他變種，如+1 或者+V（單詞表的大小）
def word_probability(word_count, total_count):
    # 使用拉普拉斯平滑
    return {word:(count+1)/(total_count+2) for word, count in word_count.items()}

# 先驗機率 prior probabilities:無條件下的比例
# 條件機率 conditional probabilities:依條件算出的機率(如單詞)
prior_spam = len(spam_emails) / (len(spam_emails) + len(ham_emails))
prior_ham = len(ham_emails) / (len(spam_emails) + len(ham_emails))
print(f"垃圾郵件先驗機率:{prior_spam}")
print(f"正常郵件先驗機率:{prior_ham}")
print("="*70)

# 計算單詞
spam_word_count = count_words(spam_emails)
ham_word_count  = count_words(ham_emails)
print(f"垃圾郵件單詞:{spam_word_count}")
print(f"正常郵件單詞:{ham_word_count}")
print("="*70)

# 計算單詞總數
total_spam_words = sum(spam_word_count.values())
total_ham_words = sum(ham_word_count.values())
print(f"垃圾郵件總單詞:{total_spam_words}")
print(f"正常郵件總單詞:{total_ham_words}")
print("="*70)

# 對郵件進行單詞機率計算
spam_word_prob = word_probability(spam_word_count, total_spam_words)
ham_word_prob = word_probability(ham_word_count, total_ham_words)
print(f"垃圾郵件字典單詞機率:{spam_word_prob}")
print(f"正常郵件字典單詞機率:{ham_word_prob}")
print("="*70)

# 測試分類器
test_email = "Claims your free gift now"
print(f"郵件:{test_email} 分類結果:{classify_email(test_email)}")
test_email = "Can we discuss your decision tomorrow"
print(f"郵件:{test_email} 分類結果:{classify_email(test_email)}")
# spam_prob:-13.1869018985419 ham_prob:-14.451858789480825
# 郵件:Claims your free gift now 分類結果:垃圾郵件
# spam_prob:-17.974393641323946 ham_prob:-14.569641825137209
# 郵件:Can we discuss your decision tomorrow 分類結果:非垃圾郵件

