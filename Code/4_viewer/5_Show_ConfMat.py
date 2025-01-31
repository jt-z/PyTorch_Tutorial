# coding: utf-8
import numpy as np
import os
import matplotlib.pyplot as plt



def show_confMat(confusion_mat, classes_name, set_name, out_dir):
    """
    可视化混淆矩阵，保存png格式
    :param confusion_mat: nd-array   n*n
    :param classes_name: list,各类别名称
    :param set_name: str, eg: 'valid', 'train'
    :param out_dir: str, png输出的文件夹
    :return:
    """
    # 归一化
    confusion_mat_N = confusion_mat.copy()
    confusion_mat_N = confusion_mat_N.astype('float32')
    for i in range(len(classes_name)):
        confusion_mat_N[i, :] = 1.0*confusion_mat[i, :] / confusion_mat[i, :].sum()

    # 获取颜色
    cmap = plt.cm.get_cmap('Blues')  # 更多颜色: http://matplotlib.org/examples/color/colormaps_reference.html
    plt.imshow(confusion_mat_N, cmap=cmap)
    plt.colorbar()

    # 设置文字
    xlocations = np.array(range(len(classes_name)))
    plt.xticks(xlocations, classes_name, rotation=60)
    plt.yticks(xlocations, classes_name)
    plt.xlabel('Predict label')
    plt.ylabel('True label')
    plt.title('Confusion_Matrix_' + set_name)

    # 打印数字
    for i in range(confusion_mat_N.shape[0]):
        for j in range(confusion_mat_N.shape[1]):
            plt.text(x=j, y=i, s=int(confusion_mat[i, j]), va='center', ha='center', color='red', fontsize=10)
    # 保存
    plt.savefig(os.path.join(out_dir, 'Confusion_Matrix_' + set_name + '.png'))
    plt.close()

if __name__ == '__main__':

    # print('QQ group: {}, password: {}'.format(671103375, 2018))

    confusion_mat = np.random.randint(low=30,high=300,size=(14, 14) )
    for i in range(14):
        confusion_mat[i, i] = 400
    # confusion_mat.dtype=np.float
    class_name = list(map(str,np.arange(6.5, 13.1, 0.5)) )
    show_confMat(confusion_mat,class_name, set_name='random',out_dir='.' )
    print('done')

