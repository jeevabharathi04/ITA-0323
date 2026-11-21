# Task B3: UI / Graphics Optimization — 60/120 FPS Frame Budgeting

## 1. The 16.6ms / 8.3ms Frame Budget
- For a smooth $60\text{ Hz}$ display, each frame must be completely measured, laid out, and rendered within $16.6\text{ ms}$.
- For a modern $120\text{ Hz}$ display, the frame budget drops to strictly **$8.3\text{ ms}$**.
- Exceeding the frame budget causes the WindowManager to drop the frame, resulting in noticeable UI stutter ("jank").

---

## 2. Techniques to Eliminate Overdraw & Layout Inefficiencies
1. **Flattening View Hierarchies:** Replace deeply nested `LinearLayout` / `RelativeLayout` trees with flat **`ConstraintLayout`** hierarchies. Reduces measurement and layout passes from $O(2^n)$ to $O(1)$.
2. **Eliminating Window Background Overdraw:** Remove unnecessary background colors on parent containers when child views completely cover the canvas (`android:windowBackground="@null"`).
3. **Lazy Inflation with ViewStub:** Defer rendering heavy UI widgets (error dialogs, empty-state screens) until they are actually needed using lightweight `ViewStub` elements.
4. **RecyclerView ViewHolder Pattern:** Reuses inflated view objects during scrolling, eliminating costly `findViewById()` calls and object allocation during animations.
