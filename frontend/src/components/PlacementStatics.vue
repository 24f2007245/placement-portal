<script setup>
</script>

<template>
    <div id="page_section">
        <div>
        <h1 style="color: #2980b9;">
            Placement Statistics
        </h1><br>
        <p>"Our placement cell consistently bridges the gap between talent and opportunity. This year, our graduates achieved a robust Average Package of 15 LPA, reflecting the high industry demand for our students. Highlighting our global reach, our Highest Package reached a staggering 4.3 Cr, marking a milestone in premier international recruitment. We’re here to ensure our students land the best opportunities possible while helping the entire professional community thrive."</p>
    </div>
    <div id="flex_box">
                <div class="two">
                    <div class="box"><p>Average Pakage</p><h2>15LPA</h2></div>
                <div class="box"><p>Highest Pakage</p><h2>4.3CrPA</h2></div>
                </div>
                <div class="two">
                    <div class="box"><p>Average Stipend</p><h2>50,000 PM</h2></div>
                <div class="box"><p>Highest Stipend</p><h2>2.5 LPM</h2></div>
                </div>
            </div><br><br>
    </div>
</template>
<style>
#flex_box{
    display: flex;
    align-items: center;
}
.two{
    display: flex;
}
.box{
    /* display: inline; */
    padding: 50px;
    /* border: 2px solid #2980b9; */
    /* width: 60px; */
    margin-left:10px ;
    margin-top: 20px;
    align-items: center;
    color: #f5f5f5;
    justify-content: center;
    background:linear-gradient(60deg,#f5f5f5, forestgreen);
}

#page_section{
    padding: 20px;
    color: gray;
}

@media(max-width:850px){
    .two{
        display: inline;
        justify-content: center;

    }
    
    #page_section {
        text-align: center;
    }
}

@media(max-width:800px){
    #flex_box{
        display: inline;
    }
}
</style>