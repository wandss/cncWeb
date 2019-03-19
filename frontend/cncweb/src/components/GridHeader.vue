<template>
    <thead>
        <tr>
            <th v-for="(item, index) in header" :key="index"
             @click.prevent.self="$emit('sort', header[index])">
                <i :class="['fa fa-sort', item ===
                 sortedColumn?'activeColumn':'regularColumn']"
                 v-if="item!=='Ações'"
                ></i>
                {{item}}
                <div id="hideColumn" @click="$emit('hideColumn', header[index])">
                    <i class='fa fa-eye-slash'></i>
                </div>
            </th>
        </tr>
        </thead>
    </template>
<script>
    export default{
        name:'GridHeader',
        props:{
            gridData:{
                type:Array,
                required:true
            },
            gridConfig:{
                type:Array,
                default:()=>[],
            },
            sortedColumn:{
                type:String,
                default:'',
            }
        },
        data(){
            return{
                originalHeader:null,
                activeColumn:{
                    'opacity':0.1,
                }
            }
        },
        computed:{
            header(){
                return this.createHeader()
            },
        },
        created(){
            this.originalHeader = this.createHeader()
        },
        methods:{
            createHeader(){
                let header = []
                if(this.gridData.length>0){
                    header = Object.keys(this.gridData[0])
                    this.gridConfig.forEach(column=>{
                        const index = header.indexOf(column.id);
                        const hidden = column.hidden===undefined?
                            false:column.hidden
                        const colName = column.colName!==undefined?
                            column.colName:column.id

                        if(index!==-1){
                            if(!hidden){
                                header[index] = colName
                            }
                            else{
                                //Removes columns when hidden is true
                                header.splice(index, 1)
                            }
                        }
                        else{
                            if(!hidden){
                                //Show hidden columns.
                                let index = this.originalHeader.indexOf(
                                    colName)
                                header.splice(index, 0,
                                    colName)
                            }
                        }
                    })
                }
                else{header = this.originalHeader}

                if(header.indexOf('rowColor')!==-1){
                    header.splice(header.indexOf('rowColor'), 1)
                }

                return header
            },
        }
  }
</script>
<style scoped>
.activeColumn{
    opacity:1;
    transition:all .2s ease-in;
}
.regularColumn{
    opacity:0.4;
}
tr{
    cursor:pointer;
}
th{
    text-transform:capitalize;
    text-align:left;
}
#hideColumn{
    float:right;
    font-size:1rem;
    opacity:.4;
}
#hideColumn:hover{
    opacity:1;
}
#sortIcon{
    opacity:0.4;
}

</style>
