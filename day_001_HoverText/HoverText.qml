import QtQuick 2.2
import QtQuick.Window 2.1


Window
{
	Text
	{
		id:text_1
		text:"hello world one"
		anchors.bottom:text_2.top
		anchors.bottomMargin:20
		anchors.horizontalCenter:text_2.horizontalCenter

		MouseArea
		{
			anchors.fill:parent
			hoverEnabled:true
			onEntered:
			{
				parent.color = "red"
				parent.font.pixelSize = 20
			}
			onExited:
			{
				parent.color = "black"
				parent.font.pixelSize = 12
			}
		}

	}

	Text
	{
		id:text_2
		text:"hello world two" 
		anchors.centerIn:parent

		MouseArea
		{
			anchors.fill:parent
			hoverEnabled:true
			onEntered:
			{
				parent.color = "red"
				parent.font.pixelSize = 20
			}
			onExited:
			{
				parent.color = "black"
				parent.font.pixelSize = 12
			}
		}
	}

	Text
	{
		id:text_3
		text:"hello world three"
		anchors.verticalCenter:text_2.verticalCenter
		anchors.verticalCenterOffset:30
		anchors.horizontalCenter:text_2.horizontalCenter


		MouseArea
		{
			anchors.fill:parent
			hoverEnabled:true
			onEntered:
			{
				parent.color = "red"
				parent.font.pixelSize = 20
			}
			onExited:
			{
				parent.color = "black"
				parent.font.pixelSize = 12
			}
		}
	}




}