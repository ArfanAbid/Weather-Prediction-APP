import React from "react";

function HourlyUpdates({ hourlyData }) {
  return (
    <div className="mt-0 p-4 text-slate-200">
      <h2 className="text-2xl mb-4 text-center font-semibold">Hourly Updates</h2>
      <div className="grid grid-cols-6 space-x-2 space-y-2">
        {hourlyData.map((updateArray, index) => (
          <div key={index} className={`border border-slate-700 p-2 rounded cursor-pointer hover:bg-slate-700 transition-colors duration-300 ease-in-out`}>
            <div className="px-2 py-1 rounded">
              {updateArray[1] ? (
                <>
                  <span className="font-bold block mb-1">{`${updateArray[1]}: ${updateArray[5]}`}</span>
                  {updateArray[6] && <img src={updateArray[6]} alt={`Weather icon for ${updateArray[1]}`} className="inline-block" />}
                </>
              ) : (
                <span className="text-red-500 block">Missing data for this update</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default HourlyUpdates;
