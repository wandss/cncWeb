<template>
    <div>
        <canvas ref="chart">
        </canvas>
    </div>
</template>
<script>
    import ChartUtils from '@/components/charts/utils';

    export default{
        name:'BarChart',
        props:{
            chartData:{
                type:Array
            },
            title:{
                type:String,
                default:''
            },
            showLegend:{
                type:Boolean,
                default:true
            },
            showTooltips:{
                type:Boolean,
                default:true,
            },
            barType:{
                type:String,
                default:'vertical',
            }

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
            showLegend(){
                this.createChart()
            },
            showTooltips(){
                this.createChart()
            }
        },
        methods:{
            createChart(){
                const chartData  = new ChartUtils(this.chartData);
                chartData.setDataset()
                const datasets = chartData.datasets;
                new this.$chart(this.$refs.chart,{
                    type:this.barType==='vertical'?'bar':'horizontalBar',
                    data:{
                        labels:datasets.labels,
                        datasets:datasets.data,
                    },
                    options:{
                        title:{
                            display:this.title.length > 0,
                            text:this.title,
                            fontSize:16,
                            fontStyle:'bold',
                        },
                        legend:{
                            display:this.showLegend,
                            position:'bottom',
                            fullWidth:true,
                        },
                        tooltips:{
                            enabled:this.showTooltips,
                        },
                        scales:{
                            yAxes:[{
                                ticks:{
                                  beginAtZero:true,
                                }
                            }],
                        },
                    }
                })
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
