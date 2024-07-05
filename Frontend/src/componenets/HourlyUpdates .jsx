import React, { useState } from "react";

function HourlyUpdates({ hourlyData }) {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpansion = () => {
    setIsExpanded(!isExpanded);
  };

  const initialItemCount = isExpanded ? hourlyData.length : Math.min(hourlyData.length, 5);

  return (
    <div className="mt-0 p-4 text-slate-200">
      <h2 className="text-2xl mb-4 text-center font-semibold">Hourly Updates</h2>

      <div className="grid grid-cols-1 md:grid-cols-5 justify-center items-center space-x-2 space-y-2">
        {hourlyData.slice(0, initialItemCount).map((updateArray, index) => (
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
      <button onClick={toggleExpansion} className="m-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        {isExpanded ? 'Show Few' : 'See More'}
      </button>
    </div>
  );
}

export default HourlyUpdates;
