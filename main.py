from math import sqrt
from math import pi
from math import exp

def dataset(filename):
    f = open(filename, 'r')
    dataset = f.read().splitlines()
    f.close()
    features = dataset[0].split(',')[:-1]
    items = []

    for i in range(1, len(dataset)):
        data = dataset[i].split(',')
        itemFeatures = {"Class": data[-1]}
        for j in range(len(features)):
            f = features[j]
            # print(f);
            v = float(data[j])
            itemFeatures[f] = v
        items.append(itemFeatures)
    return items
def naivebayes(TestData):
    filename="data.txt"
    items=dataset(filename)
    age_male = height_male = weight_male = age_female = height_female = weight_female = male = female = var_heightmale = var_weightmale = var_agemale = var_heightfemale = var_weightfemale = var_agefemale = 0

    for i in items:
        if (i['Class'] == "M"):
            male += 1
            height_male += i['Height']
            weight_male += i['Weight']
            age_male += i['Age']
        elif (i['Class'] == 'W'):
            female += 1
            height_female += i['Height']
            weight_female += i['Weight']
            age_female += i['Age']
    mean_m = {
        'h_mean': height_male/ float(male),
        'w_mean': weight_male / float(male),
        'a_mean': age_male / float(male)
    }
    mean_w = {
        'h_mean': height_female / float(female),
        'w_mean': weight_female / float(female),
        'a_mean': age_female / float(female)
    }

    for x in items:
        if (x['Class'] == 'M'):
            var_heightmale += (pow(x['Height'] - mean_m['h_mean'], 2))
            var_weightmale += (pow(x['Weight'] - mean_m['w_mean'], 2))
            var_agemale += (pow(x['Age'] - mean_m['a_mean'], 2))
        elif (x['Class'] == 'W'):
            var_heightfemale += (pow(x['Height'] - mean_w['h_mean'], 2))
            var_weightfemale += (pow(x['Weight'] - mean_w['w_mean'], 2))
            var_agefemale += (pow(x['Age'] - mean_w['a_mean'], 2))
    var_m = {
        'h_var': var_heightmale / float(male - 1),
        'w_var': var_weightmale / float(male - 1),
        'a_var': var_agemale / float(male - 1)
    }
    var_w = {
        'h_var': var_heightfemale / float(female - 1),
        'w_var': var_weightfemale / float(female - 1),
        'a_var': var_agefemale / float(female - 1)
    }


    p_m = male / len(items)
    p_w = female / len(items)

    p_hm = (1 / (sqrt(2 * pi * var_m['h_var'])) * exp(-((float(TestData['Height']) - mean_m['h_mean']) ** 2 / (2 * var_m['h_var']))))
    p_wm = (1 / (sqrt(2 * pi * var_m['w_var'])) * exp(-((float(TestData['Weight']) - mean_m['w_mean']) ** 2 / (2 * var_m['w_var']))))
    p_am = (1 / (sqrt(2 * pi * var_m['a_var'])) * exp(-((float(TestData['Age'] )- mean_m['a_mean']) ** 2 / (2 * var_m['a_var']))))

    p_hw = (1 / (sqrt(2 * pi * var_w['h_var'])) * exp(-((float(TestData['Height']) - mean_w['h_mean']) ** 2 / (2 * var_w['h_var']))))
    p_ww = (1 / (sqrt(2 * pi * var_w['w_var'])) * exp(-((float(TestData['Weight']) - mean_w['w_mean']) ** 2 / (2 * var_w['w_var']))))
    p_aw = (1 / (sqrt(2 * pi * var_w['a_var'])) * exp(-((float(TestData['Age']) - mean_w['a_mean']) ** 2 / (2 * var_w['a_var']))))

    post_m = p_m * p_hm * p_wm * p_am
    post_w = p_w * p_hw * p_ww * p_aw

    if (post_m > post_w):
        print("The predicted class is man")
    else:
        print("The predicted class is woman")

def main():
    TestData = {'Height': 168, 'Weight': 75, 'Age': 32}
    naivebayes(TestData)


if __name__ == '__main__':
    main()
