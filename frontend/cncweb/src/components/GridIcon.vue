<template>
    <div class="col-sm-3 col-md-3" title="title">
        <button @click="$emit('click')">
            {{name}}
            <span :class="icon"></span>
        </button>
    </div>
</template>
<script>
    export default{
        name:"GridIcon",
        props:{
            icon:{
                type:String,
                required:true,
            },
            name:{
                type:String,
            },
        }
    }
</script>
<style scoped>
button{
    border:none;
    background:transparent;
    font-size:1rem;
    outline:none;
    color:#3c8dbc;
}
button:hover{
    opacity:0.7;
}

</style>
