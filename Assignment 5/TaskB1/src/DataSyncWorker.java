package com.university.mobile.background;

import com.university.mobile.repository.OfflineRepository;
import java.util.List;

/**
 * Simulates a modern Android WorkManager Worker executing constraint-aware
 * background data synchronization with exponential backoff.
 */
public class DataSyncWorker {
    private final OfflineRepository repository = OfflineRepository.getInstance();

    public enum Result { SUCCESS, RETRY, FAILURE }

    public Result doWork(boolean isNetworkConnected, int attemptCount) {
        System.out.println("[DataSyncWorker] Starting background synchronization pass (Attempt: " + attemptCount + ")");
        
        if (!isNetworkConnected) {
            System.err.println("[DataSyncWorker] Constraint violated: Network unavailable. Triggering RETRY with backoff.");
            return Result.RETRY;
        }

        List<String> pending = repository.getPendingSyncIds();
        if (pending.isEmpty()) {
            System.out.println("[DataSyncWorker] No records pending synchronization. SUCCESS.");
            return Result.SUCCESS;
        }

        for (String recordId : pending) {
            String data = repository.getRecord(recordId);
            System.out.println("  -> Synchronizing record [" + recordId + "]: " + data + " to Cloud Server...");
            // Simulate network transmit
            repository.markSynced(recordId);
        }

        System.out.println("[DataSyncWorker] All pending items successfully synchronized to cloud.");
        return Result.SUCCESS;
    }
}
