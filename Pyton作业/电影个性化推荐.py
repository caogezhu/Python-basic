# 全部电影
def recommend_movies(current_watched, all_movies, other_users, top_similar=2, top_recommend=5):
    """
    为指定用户生成个性化电影推荐列表
    :param current_watched: 当前用户看过的电影集合
    :param all_movies: 总电影库集合
    :param other_users: 其他用户的观影记录字典，键为用户ID，值为观影集合
    :param top_similar: 选取的最相似用户数量
    :param top_recommend: 最终推荐的电影数量
    :return: 排序后的推荐电影列表
    """
    # 防御性校验：输入数据合法性判断
    if not isinstance(current_watched, set) or not isinstance(all_movies, set):
        raise ValueError("观影记录和总电影库必须为集合类型")
    if not isinstance(other_users, dict):
        raise ValueError("其他用户观影记录必须为字典类型")
    if not other_users:
        # 无其他用户时，从总库中选未看过的电影作为兜底
        fallback_pool = all_movies - current_watched
        return list(fallback_pool)[:top_recommend]

    # 计算每个其他用户与当前用户的雅卡尔相似度
    user_similarity = []
    for user_id, watched_set in other_users.items():
        # 过滤无效的观影记录格式
        if not isinstance(watched_set, set):
            continue
        intersection = current_watched & watched_set
        union = current_watched | watched_set
        # 避免并集为空时除零错误
        similarity = len(intersection) / len(union) if union else 0
        user_similarity.append((similarity, user_id, watched_set))

    # 按相似度从高到低排序，取前top_similar个相似用户
    user_similarity.sort(reverse=True, key=lambda x: x[0])
    similar_users = user_similarity[:top_similar]

    # 收集相似用户的所有观影记录，统计电影热度
    movie_count = {}
    for sim, _, watched_set in similar_users:
        for movie in watched_set:
            # 仅统计当前用户未看过、且在总电影库中的电影
            if movie not in current_watched and movie in all_movies:
                movie_count[movie] = movie_count.get(movie, 0) + 1

    # 按热度降序排序，取前top_recommend个电影
    sorted_recommend = sorted(movie_count.items(), key=lambda x: x[1], reverse=True)
    recommend_list = [movie for movie, count in sorted_recommend[:top_recommend]]

    # 兜底：如果推荐列表为空，从总库未看过的电影中补充
    if not recommend_list:
        fallback_pool = list(all_movies - current_watched)
        recommend_list = fallback_pool[:top_recommend]

    return recommend_list


# 示例数据
all_movies = {"流浪地球", "满江红", "奥本海默", "星际穿越", "沙丘"}
watched = {"流浪地球", "满江红"}
users = {
    "u1": {"流浪地球", "满江红", "星际穿越"},
    "u2": {"奥本海默", "沙丘", "流浪地球"},
    "u3": {"沙丘", "星际穿越"}
}

# 生成推荐列表
recommend_list = recommend_movies(watched, all_movies, users, top_similar=2, top_recommend=3)

print("推荐电影：")
if recommend_list:
    for idx, movie in enumerate(recommend_list, 1):
        print(f"{idx}. {movie}")
else:
    print("暂无符合条件的推荐电影")