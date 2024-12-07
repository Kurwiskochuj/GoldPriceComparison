import QtQuick 2.15
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: window
    visible: true
    width: 450
    height: 600
    title: "Gold Price Comparison"

    property string resultsText: ""
    property string localCurrencySymbol: ""

    font.family: "Arial" // Set default font for the application

    Rectangle {
        anchors.fill: parent
        color: "#FFFFFF"
        radius: 15
        border.color: "#DDDDDD"

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 15
            spacing: 10

            Text {
                id: titleText
                text: "Gold Price Comparison"
                font.pixelSize: 24
                font.bold: true
                color: "#FFD700" // Gold color
                horizontalAlignment: Text.AlignHCenter
                Layout.alignment: Qt.AlignHCenter
                font.family: "Arial"
            }

            // Input for Local Currency Symbol
            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Local Currency Symbol:"
                    font.pixelSize: 14
                    color: "#FFD700" // Gold color
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: localCurrencyInput
                    width: 150
                    placeholderText: "e.g., EUR, USD"
                    onTextChanged: {
                        window.localCurrencySymbol = text.trim()
                    }
                    onAccepted: exchangeRateInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Exchange Rate (" + window.localCurrencySymbol + " to THB):"
                    font.pixelSize: 14
                    color: "#FFD700" // Gold color
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: exchangeRateInput
                    width: 150
                    placeholderText: "e.g., 36,50"
                    onAccepted: localPriceInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Gold Price in Local Country (" + window.localCurrencySymbol + "/ounce):"
                    font.pixelSize: 14
                    color: "#FFD700" // Gold color
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: localPriceInput
                    width: 150
                    placeholderText: "e.g., 1.800,00"
                    onAccepted: thailandPriceInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Gold Price in Thailand (THB/Gold Baht):"
                    font.pixelSize: 14
                    color: "#FFD700" // Gold color
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: thailandPriceInput
                    width: 150
                    placeholderText: "e.g., 42.600"
                    onAccepted: investmentAmountInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Investment Amount (" + window.localCurrencySymbol + "):"
                    font.pixelSize: 14
                    color: "#FFD700" // Gold color
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: investmentAmountInput
                    width: 150
                    placeholderText: "e.g., 10.000"
                    onAccepted: calculateButton.clicked()
                }
            }

            RowLayout {
                spacing: 10
                Layout.alignment: Qt.AlignHCenter

                Button {
                    id: calculateButton
                    text: "Calculate"
                    font.family: "Arial"
                    onClicked: main.calculateResults(
                        localCurrencyInput.text,
                        exchangeRateInput.text,
                        localPriceInput.text,
                        thailandPriceInput.text,
                        investmentAmountInput.text
                    )
                }

                Button {
                    id: exitButton
                    text: "Exit"
                    font.family: "Arial"
                    onClicked: Qt.quit()
                }
            }

            ScrollView {
                Layout.fillWidth: true
                Layout.fillHeight: true

                TextArea {
                    id: resultsDisplay
                    objectName: "resultsDisplay"
                    readOnly: true
                    wrapMode: Text.Wrap
                    text: window.resultsText
                    font.family: "Arial"
                }
            }
        }
    }
}
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: window
    visible: true
    width: 450
    height: 600
    title: "Gold Price Comparison"

    property string resultsText: ""
    property string localCurrencySymbol: ""

    font.family: "Arial" // Set default font for the application

    Rectangle {
        anchors.fill: parent
        color: "#FFFFFF"
        radius: 15
        border.color: "#DDDDDD"

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 15
            spacing: 10

            Text {
                id: titleText
                text: "Gold Price Comparison"
                font.pixelSize: 24
                font.bold: true
                color: "#333333"
                horizontalAlignment: Text.AlignHCenter
                Layout.alignment: Qt.AlignHCenter
                font.family: "Arial"
            }

            // Input for Local Currency Symbol
            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Local Currency Symbol:"
                    font.pixelSize: 14
                    color: "#555555"
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: localCurrencyInput
                    width: 150
                    placeholderText: "e.g., EUR, USD"
                    onTextChanged: {
                        window.localCurrencySymbol = text.trim()
                    }
                    onAccepted: exchangeRateInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Exchange Rate (" + window.localCurrencySymbol + " to THB):"
                    font.pixelSize: 14
                    color: "#555555"
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: exchangeRateInput
                    width: 150
                    placeholderText: "e.g., 36,50"
                    onAccepted: localPriceInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Gold Price in Local Country (" + window.localCurrencySymbol + "/ounce):"
                    font.pixelSize: 14
                    color: "#555555"
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: localPriceInput
                    width: 150
                    placeholderText: "e.g., 1.800,00"
                    onAccepted: thailandPriceInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Gold Price in Thailand (THB/Gold Baht):"
                    font.pixelSize: 14
                    color: "#555555"
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: thailandPriceInput
                    width: 150
                    placeholderText: "e.g., 42.600"
                    onAccepted: investmentAmountInput.forceActiveFocus()
                }
            }

            RowLayout {
                spacing: 10
                Layout.fillWidth: true

                Label {
                    text: "Investment Amount (" + window.localCurrencySymbol + "):"
                    font.pixelSize: 14
                    color: "#555555"
                    Layout.alignment: Qt.AlignLeft
                    Layout.preferredWidth: 250
                    font.family: "Arial"
                }
                TextField {
                    id: investmentAmountInput
                    width: 150
                    placeholderText: "e.g., 10.000"
                    onAccepted: calculateButton.clicked()
                }
            }

            RowLayout {
                spacing: 10
                Layout.alignment: Qt.AlignHCenter

                Button {
                    id: calculateButton
                    text: "Calculate"
                    font.family: "Arial"
                    onClicked: main.calculateResults(
                        localCurrencyInput.text,
                        exchangeRateInput.text,
                        localPriceInput.text,
                        thailandPriceInput.text,
                        investmentAmountInput.text
                    )
                }

                Button {
                    id: exitButton
                    text: "Exit"
                    font.family: "Arial"
                    onClicked: Qt.quit()
                }
            }

            ScrollView {
                Layout.fillWidth: true
                Layout.fillHeight: true

                TextArea {
                    id: resultsDisplay
                    objectName: "resultsDisplay"
                    readOnly: true
                    wrapMode: Text.Wrap
                    text: window.resultsText
                    font.family: "Arial"
                }
            }
        }
    }
}