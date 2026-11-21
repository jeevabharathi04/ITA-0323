package com.university.mobile.repository;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.List;
import java.util.Map;

/**
 * Thread-safe offline data store simulating a local SQLite / Room repository.
 */
public class OfflineRepository {
    private static volatile OfflineRepository instance;
    private final Map<String, String> cache = new ConcurrentHashMap<>();
    private final List<String> syncQueue = new CopyOnWriteArrayList<>();

    private OfflineRepository() {}

    public static OfflineRepository getInstance() {
        if (instance == null) {
            synchronized (OfflineRepository.class) {
                if (instance == null) {
                    instance = new OfflineRepository();
                }
            }
        }
        return instance;
    }

    public void insertRecord(String id, String payload) {
        cache.put(id, payload);
        syncQueue.add(id);
    }

    public String getRecord(String id) {
        return cache.get(id);
    }

    public List<String> getPendingSyncIds() {
        return syncQueue;
    }

    public void markSynced(String id) {
        syncQueue.remove(id);
    }
}
