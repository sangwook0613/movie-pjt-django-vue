<template>
  <!-- 잘못된 경로로 접근했을 시 나타나는 페이지! -->
  <div class="center">
    <div class="center-inner">
      <div class="center-content d-flex flex-column align-items-center">
        <div class="fw-bold fs-2 mt-2">죄송합니다.</div>
        <div class="fw-bold fs-2 mt-2">요청하신 페이지를 찾을 수 없습니다.</div>
        <a href="./login" class="btn custom-btn rounded-pill fw-bold fs-5 text-white mt-4">메인 페이지로 이동</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFoundPage',
  created: function () {
    document.body.style.backgroundImage = "linear-gradient(rgba(20, 20, 20, 0.5), rgba(20, 20, 20, 0.5)), url('https://www.themoviedb.org/t/p/original/yY35sdVZtJXjeBONWH8HBXnxDgD.jpg')";
  }
}
</script>

<style scoped>
.center{
  /* background: white; */
  margin: 20px;  
}

.center-inner{ 
  position: absolute;
  top: 43%;
  left: 20%;
  right: 20%;
  background: rgba(41, 40, 40, 0.5);
  color: black;
  padding: 20px;
  transform: translateY(-50%);
  overflow: auto;
  border-radius: 8px;
}
.center-content{
  text-align: center;
  color: white;
}

.custom-btn {
  background-color: #00cecb;
  width: 250px;
}

</style>