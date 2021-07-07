import numpy as np


width, height = 640, 360

cameraPos = np.array([0, 0, 0])

imagePlane = {
    "TL": np.array([-2, 1, -1]),
    "TR": np.array([2, 1, -1]),
    "BL": np.array([-2, -1, -1]),
    "BR": np.array([2, -1, -1]),
}

# image = np.zeros((height, width, 3))
#
# for i, beta in enumerate(np.linspace(0, 1, height)):
#     for j, alpha in enumerate(np.linspace(0, 1, width)):
#
#         imagePoint = lerp(
#             lerp(imagePlane["TL"], imagePlane["TR"], alpha),
#             lerp(imagePlane["BL"], imagePlane["BR"], alpha),
#             beta
#         )
#
#         # image[i, j] = np.array([
#         #     (imagePoint[0] + 2) / 4,
#         #     (imagePoint[1] + 1) / 2,
#         #     0.5
#         # ])
#         # # print(image[i, j])
#         intersection = sphere_intersection(np.array([0, 0, -2]), 0.5, imagePoint, imagePoint - cameraPos)
#         if intersection:
#             image[i, j] = np.array([1, 0, 0])
#         # print(intersection)
#
# plt.imsave("image.png", image)
