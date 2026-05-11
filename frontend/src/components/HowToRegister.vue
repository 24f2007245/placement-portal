<script setup>
</script>

<template>
  <div style="padding: 20px;" class="max_dev">
    <h2 style="color: #3b7ca6;">Quick Guide on How to Register Yourself in the Portal</h2>
    <p style="color: chocolate;">We tried our best to keep portal simple so that everyone can get familier easily.</p>
  </div>
  <div id="registeration_process" class="max_dev">

    <div id="student">



      <div>
        <!-- <p>-> Click on "Register"</p>
        <p>-> Enter your full name and email</p>
        <p>-> Create a password</p>
        <p>-> Select role as student</p>
        <p>-> Click on register</p>
        <p>-> All set, you are allowed to login</p>
        <P>OR</P> -->
        <P>-> You can direct login via google auth</P>
        <p>-> We will store your info</p>
      </div>
      <h3>For Students</h3>

    </div>
    <div id="company">

      <div>
        <p>-> Click on register</p>
        <p>-> Enter company name/ Recruiter name</p>
        <p>-> Enter company/ Recruiter email id</p>
        <p>-> Create a password</p>
        <p>-> Click on button register</p>
        <p>-> Wait for admin approval</p>
        <p>-> once your application get approved you will able to</p>
        <p>-> Post jobs and manage applications</p>
      </div>
      <h3>For Companys</h3>

    </div>
  </div>

</template>

<style scoped>
#student div,
#company div {
  text-align: right;
}

#student,
#company {
  display: flex;
  width: 100%;
  /* flex-direction: column;    */
  align-items: center;
  justify-content: center;
  /* text-align: center; */
  margin-bottom: 30px;
}

#registeration_process {
  display: flex;
}

#registeration_process {
  color: #2980B9;
  padding: 20px;

}

#registeration_process p {
  
  color: gray;
  padding-left: 20px;
}

h3 {
  padding: 10px;
}

.max_dev{
  max-width: 1280px;
    /* width: 100%; */
    margin: 0 auto;
}

@media(max-width:780px) {
  #registeration_process {
    display: block;
  }

}
</style>