<template>
  <div class="modal-body">
    <!-- 팔로잉 유저 리스트 -->
    <div class="following_user_form">
      {% for following_list in following_list %}
      <div>
        <!-- 프로필사진, 팔로우 아이디, 메세지, 팔로잉, 팔로우 버튼-->
                <div class="following_info">
                  <div class="following_user_img">
                    <img src="{{ following_list.profile_img_src}}" alt="profile_img">
                  </div>
                  <div class="id_message">
                    <div class="following_id" > <a href="{% url 'instagram:list' following_list.following_id %}"> {{ following_list.following_id }} </a> </div>
                    <div class="following_id_message">{{ following_list.profile_msg }}</div>
                  </div>

                <div class="following_btn">
                  {% if user.username != following_list.following_id %}
                    {% if following_list.is_follow == 1 %}
                      <button type="button" class="btn btn-light" id="follow_btn" onclick="follow(this, '{{ following_list.following_id }}')">팔로잉</button>
                    {% endif %}
                    {% if following_list.is_follow == 0 %}
                      <button type="button" class="btn btn-primary" id="follow_btn" onclick="follow(this, '{{ following_list.following_id }}')">팔로우</button>
                    {% endif %}
                  {% endif %}
                </div>
                </div>
                </div>
                {% endfor %}
              </div>
            </div>
</template>

<script>
export default {

}
</script>

<style>

</style>