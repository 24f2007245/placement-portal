
<template>
    <nav>
      <span id="txt_logo" @click="indicate_index"><img src="../assets/logo.svg"></span>

      <div id="nav_right">
      
      <RouterLink to="/" class="nav_element">Home</RouterLink>
      <RouterLink to="/register" class="nav_element">Register</RouterLink>
      <RouterLink to="/login" class="nav_element">Login</RouterLink>
      
      </div>

    </nav>
</template>

<script setup>
function indicate_index(){
  window.location.href='/';
}

</script>

<style scoped>
nav{
  /* text-decoration:solid; */
  position: sticky;
  top: 0;
  color: white;
  display: flex;
  justify-content:left;
  justify-content: space-between;
  /* justify-content: space-between; */
  background-color:#2980B9;
  padding: 10px;
  z-index: 1000;
}
#nav_right{
  display: flex;
  gap: 20px;
  align-items: center;
  padding-right: 10px;

}
#txt_logo{
  display: flex;
  align-items: center;
  gap: 10px;
  padding-left: 10px;
  cursor: pointer;
}
.nav_element{
  color: #f5f5f5;
  text-decoration: none;
  /* gap: 30px; */
}
.nav_element:hover{
  color: cadetblue;
  text-decoration: overline;
}
img{
  /* overflow: hidden; */
  width: 30px;
  transform: scale(1.6);
  /* height: 30px; */
  padding-left: 10px;
}


</style>
    