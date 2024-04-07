import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, Button } from 'react-native';

const App = () => {
  // State variables for user input, matching Flask feature names
  const [pregnancies, setPregnancies] = useState('');
  const [bloodPressure, setBloodPressure] = useState('');
  const [glucose, setGlucose] = useState('');
  const [skinThickness, setSkinThickness] = useState('');
  const [insulin, setInsulin] = useState('');
  const [bmi, setBmi] = useState('');
  const [diabetesPedigreeFunction, setDiabetesPedigreeFunction] = useState('');
  const [age, setAge] = useState('');
  const [predictionText, setPredictionText] = useState('');

  const handlePrediction = async () => {
    // Construct the request payload matching Flask feature order
    const data = {
      Pregnancies: parseInt(pregnancies),
      BloodPressure: parseInt(bloodPressure),
      Glucose: parseInt(glucose),
      SkinThickness: parseInt(skinThickness),
      insulin: parseInt(insulin),
      BMI: parseFloat(bmi), // Allow decimal for BMI
      DiabetesPedigreeFunction: parseFloat(diabetesPedigreeFunction),
      age: parseInt(age),
    };

    // Make API call to the Flask endpoint
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Prediction request failed');
      }

      const result = await response.json();
      // Assuming Flask returns 'prediction_text'
      setPredictionText(result.output);
    } catch (error) {
      console.error('Prediction error:', error);
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Pregnancies"
        style={styles.input}
        value={pregnancies}
        onChangeText={setPregnancies}
        keyboardType="numeric"
      />
      {/* Other input fields go here */}

      <Button title="Run Prediction" onPress={handlePrediction} />

      <Text style={styles.prediction}>{predictionText}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    width: '80%',
    padding: 10,
    marginBottom: 10,
    borderBottomColor: '#ccc',
    borderBottomWidth: 1,
  },
  prediction: {
    marginTop: 20,
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default App;