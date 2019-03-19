<template>
    <canvas ref="chart" width="400px" height="400px">
    </canvas>
</template>
<script>
    import ChartUtils from '@/components/charts/utils';

    export default{
        name:'Bubble',
        props:{
            chartData:{
                type:Array,
                default:()=>[],
            },
            title:{
                type:String,
                default:''
            },
        },
        mounted(){
            this.createChart()
        },
        watch:{
            chartData(){
                this.createChart()
            },
            title(){
                this.createChart()
            },
        },
        methods:{
            createChart(){
                if(this.chartData.length > 0){
                    const chartData  = new ChartUtils(this.chartData)
                    chartData.setDataset('scatter')
                    const datasets = chartData.datasets;


                    console.log(datasets)
                    new this.$chart(this.$refs.chart,{
                        type:'scatter',
                        data:{
                            datasets:datasets.data,
                        },
                        options:{
                        }
                        //{
                         //   datasets:[{
                         //       data:datasets.data
                         //   }]
                            //datasets:datasets
                           // datasets:[{
                           //     data:[
                           //         {x:20, y:2, r:5},
                           //         {x:21, y:3, r:6},
                           //         {x:21.1, y:3.5, r:6},
                           //         {x:21.2, y:3.6, r:6},
                           //         {x:22, y:4, r:7}
                           //     ],
                           // }],
                       // }
                    })
                }
            },
        }
    }
</script>
<style scoped>
#chart{
    width:450px;
    height:200px;
}
</style>
