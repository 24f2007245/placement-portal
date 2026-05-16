<script setup>
</script>

<template>
    <div id="page_section">
        <div>
            <h1 style="color: #3b7ca6;">
                Placement Statistics
            </h1><br>
            <p>Our placement cell consistently bridges the gap between talent and opportunity. This year, our graduates achieved a robust Average Package of 15 LPA, reflecting the high industry demand for our students. Highlighting our global reach, our Highest Package reached a staggering 4.3 Cr, marking a milestone in premier international recruitment. We’re here to ensure our students land the best opportunities possible while helping the entire professional community thrive.</p>
        </div><br><br>
        <div id="flex_box">
                    
            <div class="box" style="background-color: #3b7ca6; color:#f5f5f5;"><p>Average Pakage</p><h2>15LPA</h2></div>
            <div class="box" style="background-color: #f5f5f5; color: #3b7ca6;"><p>Highest Pakage</p><h2>4.3CrPA</h2></div>
            
            <div class="box" style="background-color: #3b7ca6; color:#f5f5f5"><p>Average Stipend</p><h2>50,000 PM</h2></div>
            <div class="box" style="background-color: #f5f5f5; color: #3b7ca6;"><p>Highest Stipend</p><h2>2.5 LPM</h2></div>
                    
        </div><br><br>
    </div>
</template>
<style>
h1{
    /* padding-bottom: 10px; */
    padding-top: 30px;
}
#flex_box{
    display: flex;
    align-items: center;
    max-width: 1280px;
    /* width: 100%; */
    margin: 0 auto;
    justify-content: center;
}

.box{
    /* display: inline; */
    padding: 60px;
    /* border: 2px solid #2980b9; */
    /* width: 60px; */
    /* margin-left:10px ; */
    
    align-items: center;
    
    justify-content: center;
    text-align: center;
    
}

#page_section{
    padding: 25px;
    /* color: gray; */
    max-width: 1280px;
    /* width: 100%; */
    margin: 0 auto;

}



@media(max-width:800px){
    #flex_box{
        display: inline;
    }
    
}
</style>