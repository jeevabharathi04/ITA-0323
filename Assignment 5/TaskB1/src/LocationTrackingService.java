package com.university.mobile.service;

/**
 * Simulates an Android Foreground Service managing real-time continuous GPS tracking.
 */
public class LocationTrackingService {
    private boolean isRunning = false;
    private int updateIntervalMs = 5000;

    public void startForegroundService(int notificationId) {
        this.isRunning = true;
        System.out.println("[LocationService] Foreground Service started with Notification ID: " + notificationId);
        System.out.println("[LocationService] Persistent notification posted to Status Bar.");
    }

    public void setLowPowerMode(boolean enabled) {
        if (enabled) {
            this.updateIntervalMs = 60000; // Throttle to 1 min interval
            System.out.println("[LocationService] Battery low (<15%). GPS duty cycle throttled to 60s.");
        } else {
            this.updateIntervalMs = 5000;
            System.out.println("[LocationService] Normal power. High-accuracy 5s GPS tracking active.");
        }
    }

    public void stopForegroundService() {
        this.isRunning = false;
        System.out.println("[LocationService] Foreground service stopped and notification dismissed.");
    }

    public boolean isRunning() {
        return isRunning;
    }
}
