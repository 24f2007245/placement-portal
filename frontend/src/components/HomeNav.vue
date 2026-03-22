
<template>
    <nav>
      <span id="txt_logo"><strong>Placements Cell&nbsp;</strong></span>

      <div id="nav_right">
      <nav>
      <RouterLink to="/">Home</RouterLink>|
      <RouterLink to="/register">Register</RouterLink>|
      <RouterLink to="/login">Login</RouterLink>
    </nav>
    </div>

    </nav>
</template>

<script setup>

</script>

<style scoped>
nav{
  /* text-decoration:solid; */
  color: #2980B9;
  display: flex;
  justify-content:left;
  justify-content: space-between;
  /* justify-content: space-between; */
  background-color:#f5f5f5;
  padding: 10px;
}
#nav_right{
  display: flex;
  gap: 10px;
  align-items: center;

}
#txt_logo{
  font-size: larger;
}
</style>
    