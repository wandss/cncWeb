<template>
    <transition name="fade">
        <div v-show="show" id="overlay">
            <slot></slot>
        </div>
    </transition>
</template>
<script>
    export default{
        name:'Overlay',
        props:['show'],
    }
</script>
<style scoped>
#overlay{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    right:0;
    bottom:0;
    background-color:rgba(0,0,0,0.8);
    z-index:999999999999;
    overflow:auto;
}
.fade-enter-active, .fade-leave-active{
    transition: opacity .25s;
}
.fade-enter, .fade-leave-to{
    opacity: 0;
}
</style>
