import React, { useState } from 'react';

import { View, Text, StyleSheet, TextInput, Button } from 'react-native';



function LoginScreen() {

  const navigation = useNavigation();

  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');



  const handleLogin = () => {

    // Implement login functionality here

    console.log('Logging in with email:', email, 'and password:', password);

  };



  return (

    <View style={styles.container}>

      <View style={styles.loginContainer}>

        <Text style={styles.title}>Log in to sofia</Text>

        <Text style={styles.subTitle}>Sign in with Magic Link</Text>

        <Text style={styles.or}>OR</Text>

        <TextInput

          style={styles.textInput}

          onChangeText={setEmail}

          value={email}

          placeholder="Email"

          textContentType="emailAddress"

          autoCapitalize="none"

        />

        <TextInput

          style={styles.textInput}

          onChangeText={setPassword}

          value={password}

          placeholder="Password"

          textContentType="password"

          secureTextEntry={true}

        />

        <Text style={styles.forgotPassword}>Forgot password?</Text>

        <Button

          color="black"

          title="Log in with email"

          onPress={handleLogin}

        />

        <View style={styles.signUpContainer}>

          <Text style={styles.signUpText}>Don't have an account?</Text>

          <Text style={styles.signUpLink}>Sign up</Text>

        </View>

      </View>

    </View>

  );

}



const styles = StyleSheet.create({

  container: {

    flex: 1,

    justifyContent: 'center',

    alignItems: 'center',

    backgroundColor: '#fcfcfc',

  },

  loginContainer: {

    padding: 30,

    backgroundColor: '#fff',

    borderRadius: 10,

    shadowColor: '#000',

    shadowOffset: { width: 0, height: 2 },

    shadowOpacity: 0.1,

    shadowRadius: 4,

  },

  title: {

    fontSize: 30,

    fontWeight: 'bold',

    marginBottom: 20,

  },

  subTitle: {

    fontSize: 16,

    color: '#999',

    marginBottom: 20,

  },

  or: {

    fontSize: 16,

    fontWeight: 'bold',

    marginBottom: 20,

  },

  textInput: {

    height: 40,

    borderWidth: 1,

    borderColor: '#ddd',

    borderRadius: 5,

    marginBottom: 10,

    padding: 10,

  },

  forgotPassword: {

    fontSize: 12,

    color: '#999',

    marginBottom: 10,

    textAlign: 'right',

  },

  signUpContainer: {

    flexDirection: 'row',

    justifyContent: 'center',

    alignItems: 'center',

  },

  signUpText: {

    fontSize: 14,

    color: '#999',

  },

  signUpLink: {

    fontSize: 14,

    fontWeight: 'bold',

    color: '#000',

  },

});



export default LoginScreen;