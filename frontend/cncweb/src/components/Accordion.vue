<!--Change this component name to MenuItems-->
<template>
  <div id="accordion">
    <div class="card" v-for="(item, index) in accordionData" :key="index">
      <div v-for="(v, k) in item" :key="k">
        <div :class="['card-header', {'primary':k === selected }]"
         @click="selected = k" >
            {{k}}
          <span
           :class="'fa fa-chevron-'+(k === selected?'up':'down')"
           id="icon">
          </span>
        </div>

        <div :class="[k===selected?'appearEffect':'hideEffect']">
          <div class="card-body" v-show="k === selected" >
            <ul v-if="Array.isArray(v)">
              <li v-for="innerItem in v" :key="innerItem"
               @click="handleClick(innerItem)"
               @mouseover="hoveringItemName=innerItem"
               >
                {{innerItem}}
              </li>
            </ul>
            <h6 class="card-title" v-else @click="handleClick(v)">
              {{v}}
            </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default{
    name:'accordion',
    props:{
        accordionData:{
            type:Array,
            required:true,
            default:()=>[
                {Settings:['User', 'System']},
                {Languages:['Python', 'Javascript']},
                {Framework:'Django'},
            ],
        },
    },
    data(){
        return{
            selected:null,
        }
    },
    methods:{
        toggleItems(chosen){
            this.selected = chosen
        },
        handleClick(innerItem){
            /*Creates and returns an object with clicked root item and
            its chield.
            */
            let selected = {}
            selected[this.selected] = innerItem
            this.$emit('click', selected)
        },
    },

}
</script>
<style scoped>
#icon{
    float:right;
}
.card-header{
    font-weight:bold;
}
ul{
    list-style:none;
    padding-left:0;
}
li, h6{
    font-size:1.2rem;
    cursor:pointer;
}
li:hover{
    text-shadow:1px 2px 3px #333;
    transition:all .5s;
}
.card-body{
    padding:0.5rem 0rem 0rem 1rem;
    cursor:pointer;
}
.appearEffect{
    opacity:1;
    transform:translateY(0px);
    transition: opacity 1s, transform .5s;
}
.hideEffect{
    opacity:0;
    transform:translateY(-18px);
    transition: all .5s
}
.primary{
    background-color:rgba(0, 123, 255, .9);
    color:white;
    transition: all .1s;
}
.light{
    background-color:rgba(248, 249, 250, .9);
    color:black;
    transition: all .1s;
}.secondary{
    background-color:rgba(100, 117, 125, .9);
    color:white;
}
.success{
    background-color:rgba(40, 167, 69, .9);
    color:white;
}
.danger{
    background-color:rgba(220, 53, 69, .9);
    color:white;
}
.warning{
    background-color:rgba(255, 193, 7, .9);
    color:black;
}
.info{
    background-color:rgba(23, 162, 184, .9);
    color:white;
}
.dark{
    background-color:rgba(52, 58, 64, .9);
    color:white;
}
.white{
    background-color:rgba(255, 255, 255, .9);
    color:black;
}

</style>
