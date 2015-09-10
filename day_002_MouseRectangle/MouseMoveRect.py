import QtQuick 2.2

Rectangle
{
	id : wnd
	width:600
	height:600
	property int zValue : 0

	Rectangle
	{
		id : blue
		x : 40
		y : 40
		z : 0
		width : 200
		height : 200
		color : "#a00000ff"
		property int xPress : 0
		property int yPress : 0

		MouseArea
		{
			anchors.fill:parent
			onPressed : 
			{
				blue.z = ++wnd.zValue
				blue.xPress = mouse.x
				blue.yPress = mouse.y
			}
			onPositionChanged : 
			{
				blue.x += mouse.x - blue.xPress
				blue.y += mouse.y - blue.yPress
			}
		}

	}

	Rectangle
	{
		id : red
		x : 200
		y : 200
		z : 0
		width : 200
		height : 200
		color : "#a0ff0000"
		property int xPress : 0
		property int yPress : 0
		MouseArea
		{
			anchors.fill:parent
			onPressed : 
			{
				red.z = ++wnd.zValue
				red.xPress = mouse.x
				red.yPress = mouse.y
			}
			onPositionChanged : 
			{
				red.x += mouse.x - red.xPress
				red.y += mouse.y - red.yPress
			}
		}

	}

	Rectangle
	{
		id : green
		x : 360
		y : 360
		z : 0
		width : 200
		height : 200
		color : "#a000ff00"
		property int xPress : 0
		property int yPress : 0
		MouseArea
		{
			anchors.fill:parent
			onPressed : 
			{
				green.z = ++wnd.zValue
				green.xPress = mouse.x
				green.yPress = mouse.y
			}
			onPositionChanged : 
			{
				green.x += mouse.x - green.xPress
				green.y += mouse.y - green.yPress
			}
		}

	}


}