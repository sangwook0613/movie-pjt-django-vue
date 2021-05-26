<template>
  <!-- 잘못된 경로로 접근했을 시 나타나는 페이지! -->
  <div class="center">
    <div class="center-inner">
      <div class="center-content">
        <h1> 죄송합니다.</h1>
        <h1> 요청하신 페이지를 찾을 수 없습니다.</h1>
        <a href="./login" class="btn btn-light btn mt-2">메인 페이지로 이동</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFoundPage',
}
</script>

<style scoped>
.center{
  /* background: white; */
  margin: 20px;  
}
 .center-inner{ 
  position: absolute;
  top: 50%;
  left: 20%;
  right: 20%;
  background: red;
  color: black;
  padding: 20px;
  transform: translateY(-50%);
  resize: vertical;
  overflow: auto;
  
}
.center-content{
  text-align: center;
  color: white;
  
}
</style>