name=input('请输入您的名字：')
s1=int(input('请输入你上一次的考试成绩：'))
s2=int(input('请输入你本次的考试成绩：'))

print('...')

r=(s2-s1)/s2*100

if s2>s1:
    print('恭喜你,%s的成绩上升了%.1f%%'%(name,r))
elif s2==s1:
    print('似乎这次%s的考试没有进步噢,下次请加油'%name)
else:
    print('很遗憾，%s的成绩下降了%.1f%%，下次请加油哦～'%(name,r))