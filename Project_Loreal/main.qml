import QtQuick 2.12
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 400
    height: 650
    visible: true
    color: "#00000000"
    title: qsTr("")


    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex













        Page1Form {
            Rectangle {
                id: rectangle
                width: 400
                height: 650
                radius: 0
                border.color: "#f7e5e5"
                gradient: Gradient {
                    GradientStop {
                        position: 0.80654
                        color: "#8fa381"
                    }

                    GradientStop {
                        position: 1
                        color: "#e7eae5"
                    }
                }
                Image {
                    id: image
                    x: 100
                    y: 39
                    width: 200
                    height: 200
                    source: "images/logo.png"
                    fillMode: Image.PreserveAspectFit
                }

                Rectangle {
                    id: rectangle3
                    x: 95
                    y: 283
                    width: 205
                    height: 27
                    color: "#ffffff"
                    radius: 5
                    TextInput {
                        id: textInput
                        x: 3
                        y: 3
                        width: 199
                        height: 27
                        text: qsTr("")
                        font.pixelSize: 15
                    }
                }

                Text {
                    id: text1
                    x: 49
                    y: 288
                    text: qsTr("Name")
                    font.pixelSize: 14
                    font.bold: true
                }

                Text {
                    id: text2
                    x: 49
                    y: 345
                    text: qsTr("Age")
                    font.pixelSize: 14
                    font.bold: true
                }

                ComboBox {
                    id: comboBox
                    x: 95
                    y: 342
                    width: 103
                    height: 25
                    editable: true
                    font.pointSize: 8
                    model: ListModel {
                        id: model
                        ListElement { text: "" }
                        ListElement { text: "14" }
                        ListElement { text: "15" }
                        ListElement { text: "16" }
                        ListElement { text: "17" }
                        ListElement { text: "18" }
                        ListElement { text: "19" }
                        ListElement { text: "20" }
                        ListElement { text: "21" }
                        ListElement { text: "22" }
                        ListElement { text: "23" }
                        ListElement { text: "24" }
                        ListElement { text: "25" }
                        ListElement { text: "26" }
                        ListElement { text: "27" }
                        ListElement { text: "28" }
                        ListElement { text: "29" }
                        ListElement { text: "30" }
                        ListElement { text: "31" }
                        ListElement { text: "32" }
                        ListElement { text: "33" }
                        ListElement { text: "34" }
                        ListElement { text: "35" }
                        ListElement { text: "36" }
                        ListElement { text: "37" }
                        ListElement { text: "38" }
                        ListElement { text: "39" }
                        ListElement { text: "40" }
                        ListElement { text: "41" }
                        ListElement { text: "42" }
                        ListElement { text: "43" }
                        ListElement { text: "44" }
                        ListElement { text: "45" }
                        ListElement { text: "46" }
                        ListElement { text: "47" }
                        ListElement { text: "48" }
                        ListElement { text: "49" }
                        ListElement { text: "50" }
                        ListElement { text: "51" }
                        ListElement { text: "52" }
                        ListElement { text: "53" }
                        ListElement { text: "54" }
                        ListElement { text: "55" }
                        ListElement { text: "56" }
                        ListElement { text: "57" }
                        ListElement { text: "58" }
                        ListElement { text: "59" }
                        ListElement { text: "60" }
                    }
                    onActivated: {
                        user.set_patient_age(comboBox.currentValue)
                    }

                }

                Text {
                    id: text3
                    x: 178
                    y: 498
                    text: qsTr("Gender")
                    font.pixelSize: 14
                    font.bold: true
                }

                RoundButton {
                    id: roundButton
                    x: 77
                    y: 405
                    width: 90
                    height: 87
                    visible: true
                    text: "+"
                    onClicked:
                    {
                        user.set_Gender('Man')
                        gender.text = "Man"
                    }

                }

                RoundButton {
                    id: roundButton1
                    x: 235
                    y: 405
                    width: 90
                    height: 87
                    opacity: 1
                    visible: true
                    text: "+"
                    onClicked:
                    {
                        user.set_Gender('Woman')
                        gender.text = "Woman"
                    }
                }

                Image {
                    id: image1
                    x: 235
                    y: 399
                    width: 100
                    height: 100
                    source: "images/Women.png"
                    fillMode: Image.PreserveAspectFit
                }

                Image {
                    id: image2
                    x: 72
                    y: 399
                    width: 100
                    height: 100
                    source: "images/Man.png"
                    fillMode: Image.PreserveAspectFit
                }

                Image {
                    id: image3
                    x: 156
                    y: 517
                    width: 100
                    height: 98
                    source: "images/LOreal-Logo.png"
                    fillMode: Image.PreserveAspectFit
                }

                Text {
                    id: gender
                    x: 113
                    y: 379
                    width: 181
                    height: 14
                    horizontalAlignment: Text.AlignHCenter
                    font.bold: true
                }

                RoundButton {
                    id: button7
                    x: 311
                    y: 282
                    width: 59
                    height: 29
                    text: qsTr("Enter")
                    onClicked: {
                        user.set_patient_name(textInput.text)
                    }
                }
            }
        }








        Page2Form {
            Rectangle {
                id: rectangle1
                width: 400
                height: 650
                radius: 0
                gradient: Gradient {
                    GradientStop {
                        position: 0.80841
                        color: "#8fa381"
                    }

                    GradientStop {
                        position: 1
                        color: "#e7eae5"
                    }
                }
                Image {
                    id: image11
                    x: 44
                    y: -25
                    width: 313
                    height: 174
                    source: "images/take_your_time.png"
                    fillMode: Image.PreserveAspectFit
                }

                Rectangle {
                    id: rectangle4
                    x: 29
                    y: 120
                    width: 343
                    height: 318
                    color: "#c0baba"
                    radius: 10

                    Image {
                        id: image9
                        x: 6
                        y: 9
                        width: 330
                        height: 299
                        visible: false
                        source: "image.png"
                        asynchronous: true
                        cache: false
                        fillMode: Image.PreserveAspectFit
                    }
                }


                RoundButton {
                    id: roundButton2
                    x: 161
                    y: 451
                    width: 77
                    height: 74
                    text: "+"
                    onClicked: {
                        webcam.image('1')
                    }
                }


                Image {
                    id: image10
                    x: 161
                    y: 444
                    width: 78
                    height: 89
                    source: "images/Camara.png"
                    fillMode: Image.PreserveAspectFit
                }

            }
        }

        Page3Form {
            id: page3Form

            Rectangle {
                id: rectangle2
                width: 400
                height: 650
                radius: 0
                gradient: Gradient {
                    GradientStop {
                        position: 0.80841
                        color: "#8fa381"
                    }

                    GradientStop {
                        position: 1
                        color: "#e7eae5"
                    }
                }
                Image {
                    id: image4
                    x: 57
                    y: 0
                    width: 280
                    height: 567
                    source: "images/Body.PNG"
                    RoundButton {
                        id: button
                        x: -6
                        y: 414
                        width: 108
                        height: 32
                        text: qsTr("Lower extremity")
                        font.pointSize: 10
                        checkable: true
                        highlighted: false
                        onClicked: {
                            user.set_location(button.text)
                        }
                    }

                    RoundButton {
                        id: button1
                        x: 101
                        y: 270
                        width: 84
                        height: 28
                        text: qsTr("Genitals")
                        font.pointSize: 10
                        checkable: true
                        onClicked: {
                            user.set_location(button1.text)
                        }
                    }

                    RoundButton {
                        id: button2
                        x: 209
                        y: 155
                        width: 108
                        height: 30
                        text: qsTr("Upper extremity")
                        font.pointSize: 10
                        layer.enabled: false
                        checkable: true
                        checked: false
                        highlighted: false
                        onClicked: {
                            user.set_location(button2.text)
                        }
                    }

                    RoundButton {
                        id: button3
                        x: 208
                        y: 286
                        width: 84
                        height: 28
                        text: qsTr("Palms")
                        font.pointSize: 10
                        checkable: true
                        onClicked: {
                            user.set_location(button3.text)
                        }
                    }

                    RoundButton {
                        id: button4
                        x: 8
                        y: 100
                        width: 110
                        height: 28
                        text: qsTr("Head / Neck")
                        font.pointSize: 10
                        wheelEnabled: false
                        checkable: true
                        onClicked: {
                            user.set_location(button4.text)
                        }
                    }

                    RoundButton {
                        id: button5
                        x: 103
                        y: 140
                        width: 77
                        height: 28
                        text: qsTr("Torso")
                        font.pointSize: 10
                        checked: false
                        onClicked: {
                            user.set_location(button5.text)
                        }
                    }

                    RoundButton {
                        id: button6
                        x: 220
                        y: 494
                        width: 97
                        height: 28
                        text: qsTr("Unknown")
                        font.pointSize: 10
                        checkable: true
                        highlighted: false
                        onClicked: {
                            user.set_location(button6.text)
                        }
                    }
                    fillMode: Image.PreserveAspectFit
                }

                Image {
                    id: image5
                    x: -96
                    y: 175
                    width: 288
                    height: 154
                    source: "images/location.png"
                    rotation: 270
                    fillMode: Image.PreserveAspectFit
                }
            }
        }

        Page4Form {
            id: page4Form


            Rectangle {
                id: rectangle5
                width: 400
                height: 650
                radius: 0
                gradient: Gradient {
                    GradientStop {
                        position: 0.80607
                        color: "#8fa381"
                    }

                    GradientStop {
                        position: 1
                        color: "#e7eae5"
                    }
                }
                Image {
                    id: image6
                    x: 29
                    y: 441
                    width: 80
                    height: 92
                    source: "images/prevent.png"
                    fillMode: Image.PreserveAspectFit
                }

                Image {
                    id: image7
                    x: 274
                    y: 441
                    width: 100
                    height: 100
                    source: "images/LOreal-Logo.png"
                    fillMode: Image.PreserveAspectFit
                }

                Image {
                    id: image8
                    x: 91
                    y: 45
                    width: 219
                    height: 178
                    source: "images/health.png"
                    fillMode: Image.PreserveAspectFit
                }

                Rectangle {
                    id: rectangle6
                    x: 39
                    y: 287
                    width: 323
                    height: 45
                    color: "#ffffff"
                }

                Text {
                    id: text6
                    x: 109
                    y: 295
                    width: 187
                    height: 29
                    text: qsTr("")
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    font.bold: true
                }

                Text {
                    id: text4
                    x: 155
                    y: 255
                    width: 117
                    height: 26
                    text: qsTr("Your Result:")
                    font.pixelSize: 15
                    font.bold: true
                }

                Text {
                    id: text5
                    x: 104
                    y: 402
                    width: 192
                    height: 26
                    text: qsTr("Healthy body.  Healthy life.")
                    font.pixelSize: 15
                    font.bold: true
                }

                RoundButton {
                    id: button9
                    x: 164
                    y: 349
                    width: 73
                    height: 32
                    text: qsTr("Search")
                    font.italic: true
                    onClicked: {
                        app_model.search_result(button.action)
                    }
                }

            }

            Text {
                id: text7
                x: -31
                y: 528
                width: 463
                height: 60
                text: qsTr("Warning
This application is not 100% accurate.
The results shown cannot replace a professional diagnosis.
For a full revision, please visit a health care professional.
The information you provide will be saved and analyzed by a specialist,
 to further improve our application.")
                font.pixelSize: 8
                horizontalAlignment: Text.AlignHCenter
                minimumPixelSize: 9
                font.bold: false
            }
        }
    }

    Connections {
        target: user
        // Signal Handler
        onUserGender: gender.text = user_gender_tx
    }
    Connections {
        target: app_model
        // Signal Handler
        onUserResult: text6.text = user_result_tx
    }

    Connections {
        target: webcam
        // Signal Handler
        onUserImage:
        {
            image9.visible = true
            image9.source = user_image_tx
            image9.update()
        }
    }

    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

        TabButton {
            text: qsTr("Profile")
        }
        TabButton {
            text: qsTr("Detection")
        }
        TabButton {
            text: qsTr("Location")
        }
        TabButton {
            text: qsTr("Result")
        }
    }
}
