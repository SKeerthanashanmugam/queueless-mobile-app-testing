package com.keerthana.queueless

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.keerthana.queueless.ui.theme.QueuelessTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            QueuelessTheme {
                Surface(modifier = Modifier.fillMaxSize()) { QueueLessApp() }
            }
        }
    }
}

data class Doctor(
    val name: String,
    val specialty: String,
    val experience: String,
    val hospital: String,
    val languages: String,
    val fee: Int,
    val slot: String
)

private val doctors = listOf(
    Doctor("Dr. Meena Raman", "Cardiology", "8 years", "City Care Hospital, Vellore", "English, Tamil", 500, "Tomorrow, 10:30 AM"),
    Doctor("Dr. Arjun Kumar", "Dermatology", "6 years", "Apollo Clinic, Vellore", "English, Tamil", 400, "Tomorrow, 11:00 AM"),
    Doctor("Dr. Priya Lakshmi", "Pediatrics", "10 years", "Rainbow Children's Clinic", "English, Tamil, Telugu", 600, "Tomorrow, 2:30 PM"),
    Doctor("Dr. Karthik Raj", "Orthopedics", "7 years", "Vellore Ortho Centre", "English, Tamil", 550, "Friday, 9:30 AM"),
    Doctor("Dr. Nandhini S", "Gynecology", "9 years", "Women's Wellness Hospital", "English, Tamil", 650, "Friday, 4:00 PM")
)

@Composable
fun QueueLessApp() {
    var screen by remember { mutableStateOf("login") }
    var mobile by remember { mutableStateOf("") }
    var otp by remember { mutableStateOf("") }
    var error by remember { mutableStateOf("") }
    var search by remember { mutableStateOf("") }
    var selectedDoctor by remember { mutableStateOf(doctors.first()) }
    var bookedDoctor by remember { mutableStateOf<Doctor?>(null) }
    var paid by remember { mutableStateOf(false) }

    when (screen) {
        "login" -> LoginScreen(mobile, { mobile = it; error = "" }, error) {
            if (mobile.length == 10 && mobile.all(Char::isDigit)) screen = "otp"
            else error = "Enter a valid 10-digit mobile number"
        }
        "otp" -> OtpScreen(otp, { otp = it; error = "" }, error,
            onVerify = {
                if (otp == "123456") screen = "home"
                else error = "Invalid OTP. Use test OTP 123456"
            },
            onBack = { otp = ""; error = ""; screen = "login" }
        )
        "home" -> HomeScreen(search, { search = it }, bookedDoctor,
            onDoctorSelected = { selectedDoctor = it; screen = "doctor" },
            onViewAppointment = { screen = "appointment" },
            onLogout = { mobile = ""; otp = ""; search = ""; error = ""; screen = "login" }
        )
        "doctor" -> DoctorScreen(selectedDoctor, { screen = "home" }) {
            bookedDoctor = selectedDoctor
            paid = false
            screen = "appointment"
        }
        "appointment" -> bookedDoctor?.let { doctor ->
            AppointmentScreen(doctor, paid, { screen = "home" }, { paid = true }) {
                bookedDoctor = null
                paid = false
                screen = "home"
            }
        } ?: run { screen = "home" }
    }
}

@Composable
private fun LoginScreen(mobile: String, onMobileChange: (String) -> Unit, error: String, onContinue: () -> Unit) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.Center) {
        Text("QueueLess", style = MaterialTheme.typography.headlineLarge, fontWeight = FontWeight.Bold)
        Text("Smart hospital appointments without waiting", modifier = Modifier.padding(top = 8.dp, bottom = 32.dp))
        OutlinedTextField(
            value = mobile,
            onValueChange = { if (it.length <= 10) onMobileChange(it) },
            label = { Text("Mobile number") },
            singleLine = true,
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Phone),
            modifier = Modifier.fillMaxWidth().testTag("mobile-number")
        )
        ErrorText(error)
        Button(onContinue, Modifier.fillMaxWidth().padding(top = 20.dp).testTag("continue-button")) { Text("Continue") }
        Text("Testing note: Use any valid 10-digit number.", style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(top = 16.dp))
    }
}

@Composable
private fun OtpScreen(otp: String, onOtpChange: (String) -> Unit, error: String, onVerify: () -> Unit, onBack: () -> Unit) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.Center) {
        Text("Verify OTP", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
        Text("Enter the six-digit test OTP", modifier = Modifier.padding(top = 8.dp, bottom = 24.dp))
        OutlinedTextField(
            value = otp,
            onValueChange = { if (it.length <= 6) onOtpChange(it) },
            label = { Text("OTP") },
            singleLine = true,
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword),
            modifier = Modifier.fillMaxWidth().testTag("otp-input")
        )
        ErrorText(error)
        Button(onVerify, Modifier.fillMaxWidth().padding(top = 20.dp).testTag("verify-otp-button")) { Text("Verify OTP") }
        TextButton(onBack, Modifier.align(Alignment.CenterHorizontally)) { Text("Change mobile number") }
        Text("Test OTP: 123456", style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(top = 12.dp))
    }
}

@Composable
private fun ErrorText(error: String) {
    if (error.isNotEmpty()) Text(error, color = MaterialTheme.colorScheme.error, modifier = Modifier.padding(top = 8.dp).testTag("validation-error"))
}

@Composable
private fun HomeScreen(
    search: String,
    onSearchChange: (String) -> Unit,
    bookedDoctor: Doctor?,
    onDoctorSelected: (Doctor) -> Unit,
    onViewAppointment: () -> Unit,
    onLogout: () -> Unit
) {
    val results = doctors.filter {
        search.isBlank() || it.name.contains(search, true) || it.specialty.contains(search, true) || it.hospital.contains(search, true)
    }
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
            Text("Find a Doctor", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold, modifier = Modifier.testTag("home-title"))
            TextButton(onLogout) { Text("Logout") }
        }
        OutlinedTextField(
            value = search,
            onValueChange = onSearchChange,
            label = { Text("Search doctor, specialty or hospital") },
            singleLine = true,
            modifier = Modifier.fillMaxWidth().padding(top = 20.dp).testTag("doctor-search")
        )
        bookedDoctor?.let { doctor ->
            Card(Modifier.fillMaxWidth().padding(top = 20.dp)) {
                Column(Modifier.padding(16.dp)) {
                    Text("Upcoming Appointment", fontWeight = FontWeight.Bold)
                    Text("${doctor.name} • ${doctor.specialty}")
                    Text(doctor.slot)
                    Button(onViewAppointment, Modifier.padding(top = 12.dp)) { Text("View Appointment") }
                }
            }
        }
        Text("Available Doctors (${results.size})", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, modifier = Modifier.padding(top = 28.dp, bottom = 12.dp))
        if (results.isEmpty()) {
            Text("No doctors found. Try another name, specialty or hospital.", modifier = Modifier.testTag("empty-search-result"))
        } else {
            results.forEach { doctor ->
                DoctorCard(doctor) { onDoctorSelected(doctor) }
                Spacer(Modifier.height(12.dp))
            }
        }
    }
}

@Composable
private fun DoctorCard(doctor: Doctor, onClick: () -> Unit) {
    Card(onClick = onClick, modifier = Modifier.fillMaxWidth().testTag("doctor-result-card")) {
        Column(Modifier.padding(18.dp)) {
            Text(doctor.name, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
            Text("${doctor.specialty} • ${doctor.experience} experience")
            Text(doctor.hospital)
            Text("Consultation fee: ₹${doctor.fee}")
            Text("Next available: ${doctor.slot}", color = MaterialTheme.colorScheme.primary, modifier = Modifier.padding(top = 8.dp))
        }
    }
}

@Composable
private fun DoctorScreen(doctor: Doctor, onBack: () -> Unit, onBook: () -> Unit) {
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TextButton(onBack) { Text("← Back") }
        Text(doctor.name, style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold, modifier = Modifier.padding(top = 16.dp))
        Text(doctor.specialty)
        Text("${doctor.experience} experience")
        Text(doctor.hospital)
        Text("Languages: ${doctor.languages}")
        Text("Consultation fee: ₹${doctor.fee}")
        Text("Available Slot", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, modifier = Modifier.padding(top = 32.dp, bottom = 16.dp))
        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(18.dp)) {
                Text(doctor.slot, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                Button(onBook, Modifier.fillMaxWidth().padding(top = 16.dp).testTag("book-appointment")) { Text("Book Appointment") }
            }
        }
    }
}

@Composable
private fun AppointmentScreen(doctor: Doctor, paid: Boolean, onBack: () -> Unit, onPay: () -> Unit, onCancel: () -> Unit) {
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TextButton(onBack) { Text("← Home") }
        Text("Appointment Confirmed", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold, modifier = Modifier.padding(top = 16.dp))
        Card(Modifier.fillMaxWidth().padding(top = 24.dp)) {
            Column(Modifier.padding(18.dp)) {
                Text("Booking ID: QL-1001")
                Text("Doctor: ${doctor.name}")
                Text("Specialty: ${doctor.specialty}")
                Text("Slot: ${doctor.slot}")
                Text("Hospital: ${doctor.hospital}")
                Text("Fee: ₹${doctor.fee}")
                Text(
                    if (paid) "Payment Status: PAID" else "Payment Status: PENDING",
                    fontWeight = FontWeight.Bold,
                    color = if (paid) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.error,
                    modifier = Modifier.padding(top = 16.dp).testTag("payment-status")
                )
            }
        }
        if (!paid) {
            Button(onPay, Modifier.fillMaxWidth().padding(top = 24.dp).testTag("pay-button")) { Text("Pay ₹${doctor.fee}") }
        } else {
            Text("Payment successful. Transaction ID: TXN-5001", color = MaterialTheme.colorScheme.primary, modifier = Modifier.padding(top = 24.dp))
        }
        OutlinedButton(onCancel, Modifier.fillMaxWidth().padding(top = 16.dp).testTag("cancel-appointment")) { Text("Cancel Appointment") }
    }
}
