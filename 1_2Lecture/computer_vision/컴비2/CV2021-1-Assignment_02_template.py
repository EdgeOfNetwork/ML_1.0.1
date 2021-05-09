
'''
Problem #1 Feature Descriptor and Feature Matching (40 pts)
'''

# Problem 1-1

# 이미지를 읽고, 파라미터를 설정하세요.
image = None
width = None
height = None
stride = None

def make_patches(image, width, height, stride):
    # 패치란 본래의 이미지보다 작은 이미지를 의미합니다.
    # 이미지의 KeyPoint 추출 및 Descriptor의 입력으로 이미지 전체가 아닌, 작은 패치를 주어야 합니다.
    # 이를 위한 기본 전처리 작업 함수라고 생각하시면 됩니다.
    # 또한, 이 함수의 결과 자체도 하나의 Descriptor 특징으로 사용될 수 있습니다 (문제에서 "image patch" 디스크립터라 칭함).
    # image는 우리가 작게 쪼개고자 하는 원본 이미지이며,
    # width, height는 만들고자 하는 패치의 가로, 세로의 크기입니다.
    # cv2 imread는 이미지를 Height, Width, Channel 형식으로 읽으므로 슬라이싱 시 주의하세요.
    # stride는 crop 시, 얼마 만큼의 간격으로 자를 것인지를 나타냅니다. 만약 stride=1이라면 1 pixel 간격으로 가장 dense하게 자르게 됩니다.

    patches = list()
    keypoints = list()
    H, W, _ = image.shape
    # 패치를 자르는 알고리즘을 구성하세요.
    # for 문 사용 시, H -> W 순으로 이중 for 문을 사용해 슬라이싱 하길 권장합니다.
    # cv2는 기본적으로 이미지를 (H, W, C) 형태로 취급합니다.
    # 슬라이싱 시에 패치의 중앙 위치 (원본 이미지 기준)를 따로 리스트에 담아 두어야 1-3) 문제 풀이가 가능합니다.
    # ...과 None 등은 직접 채우셔야 합니다.
    for h_i in range(...):
        for w_i in range(...):
            # 패치를 슬라이싱 하세요.
            patch = None

            # h_i, w_i를 이용하여, 원본 이미지 상에서 패치의 중앙점의 좌표를 구하세요.
            center_x = None
            center_y = None
            # cv2.KeyPoint 객체를 생성하세요. 아래는 하나의 예시입니다.
            keypoint = cv2.KeyPoint(center_x, center_y, size=(width + height) / 2.0)

            patches.append(patch)
            keypoints.append(keypoint)

    return patches, keypoints

# 결과로 나온 패치들은 (# of patches, h, w, 3)와 같은 형태가 되어야 합니다.
# h와 w 순서는 바뀔 수 있으나, (h, w) 순으로 구성하는 것이 추후 cv2 함수 사용 시 편합니다.
patches, keypoints = make_patches(image, width, height, stride)

# Problem 1-2
def extract_gradients(patch):
    # 주어진 이미지(패치)의 gradient를 구하는 알고리즘을 구성하세요.
    # X, Y의 gradient 외에 여러 gradient 계열(코너 등)의 특징 모두 가능합니다.
    # cv2 라이브러리를 사용하셔도 됩니다.
    grads = None

    return grads

def extract_color_histogram(patch):
    # 주어진 이미지(패치)의 컬러 히스토그램을 추출하세요.
    # bin 개수 등은 자율적으로 선택하세요.
    # cv2 라이브러리를 사용하셔도 됩니다.
    hists = None

    return hists

# Problem 1-3
# 1) 임의의 두 페어 이미지를 읽고 패치를 추출하세요.
patches_01 = None
patches_02 = None

# 2) 추출한 패치들을 이용하여 디스크립터를 추출하세요.
patch_features_01 = list()
gradients_01 = list()
histograms_01 = list()
for patch in patches_01:
    # 각 패치마다, 1-2)에서 구현한 함수를 활용하여, 그라디언트와 컬러 히스토그램을 추출하세요.
    patch_feature = patch
    grad = None
    hist = None
    # 특징이 여러 랭크를 가지고 있다면 1개의 랭크가 되도록 reshape 하세요.
    # 예를 들어, grads가 (A, B, C) 차원이라면 (A * B * C, ) 차원이 되도록 하세요.
    # 아래 ...은 채우셔야 합니다.
    # reshape이 필요 없다면 넘어가시면 됩니다.
    patch_feature = np.reshape(...)
    grad = np.reshape(...)
    hist = np.reshape(...)

    patch_features_01.append(np.array(patch_feature, dtype=np.float32))
    gradients_01.append(np.array(grad, dtype=np.float32))
    histograms_01.append(np.array(hist, dtype=np.float32))

# 두 번째 이미지에 대해서도 똑같이 추출합니다.

# 3) 추출된 특징을 이용하여, 매칭을 수행하세요.
# cv2의 BruteForce Matcher와 같은 함수를 이용해 진행하시면 됩니다.
matcher = cv2.BFMatcher(...)

matches = matcher.match(...)

# match 결과를 모두 plot 할 수 없으므로, distance와 같은 기준으로 sorting 하여
# 가까운 matching 10~50개 정도 만을 가지고 결과를 그리시는 게 좋습니다.
draw_image = cv2.drawMatches(...)

# Problem 1-4
# cv2의 라이브러리 함수를 활용하여, SIFT와 같은 특징을 추출하세요.
# 그리고, 1-3과 유사하게 매칭과 결과를 그려보세요.

'''
Problem #2 Homography and Stitching (30 pts)
'''

# Problem 2-1
# 1) 1-4의 매칭 포인트들을 이용하여, cv2.findHomography를 사용해, Homography 행렬을 SVD 방식으로 구해보세요.

# 먼저, 임의의 paired 이미지를 읽습니다.
image_01 = None
image_02 = None

# cv2 함수에서 SIFT와 같은 디스크립터를 정의하세요.
descriptor = None

# 두 이미지에 대하여, Keypoint와 특징을 추출하세요.
keypoints_01, features_01 = ...
keypoints_02, features_02 = ...

# 위 포인트들에 대하여 1-3~4와 유사하게 매칭을 수행합니다.
matcher = cv2.BFMatcher(...)

raw_matches = matcher.match(...)

# 위 matches를 모두 사용하면 outlier 때문에 homography 추출이 올바르지 않을 가능성이 큽니다.
# 따라서, 본인이 생각한 기준으로 raw_matches 중 좋은 매칭 결과를 선별해줍니다.

good_matches = None

# 위 결과로 Homoraphy 행렬을 구합니다.
H, ok = cv2.findHomography(...)

# Problem 2-2
# 2-1의 matches를 이용하여, RANSAC option으로 H를 구해보세요.

# Problem 2-3
# cv2.warpPersective 함수를 이용하여 2-1)과 2-2)의 결과를 나타내어 비교해보세요.

'''
Problem #3 Homography with RANSAC 직접 구현 (30 pts)
'''

# 2-1)과 2-2)에서 사용한 matches를 기반으로, Homography를 RANSAC 알고리즘을 통해 구해보세요.
# 이 때, cv2.findHomography와 같은 Homography 행렬을 직접적으로 구해주는 라이브러리는 사용하시면 안됩니다.
# numpy의 svd 계산 등과 같이 중간 과정을 위한 라이브러리 사용은 가능합니다.