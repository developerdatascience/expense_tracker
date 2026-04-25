from streamlit_echarts import st_echarts


def pie_chart(data):
    option = {
        "tooltip": {"trigger": "item"},
        "series": [
            {
                "type": "pie",
                "data": [
                    {"value": d["total"], "name": str(d["category_id"])}
                    for d in data
                ]
            }
        ]
    }
    st_echarts(option, height="400px")


def line_chart(data):
    option = {
        "xAxis": {
            "type": "category",
            "data": [d["date"] for d in data]
        },
        "yAxis": {"type": "value"},
        "series": [{
            "data": [d["total"] for d in data],
            "type": "line",
            "smooth": True
        }]
    }
    st_echarts(option, height="400px")
